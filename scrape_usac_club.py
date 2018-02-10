import bs4
import datetime
import re
import sys
import urllib


BASE_URL = 'https://legacy.usacycling.org'
CLUB_URL_TEMPLATE = BASE_URL + '/clubs/members.php?club=%s'
RESULTS_URL_TEMPLATE = BASE_URL + '/results/?compid=%s'


def extract_first_row(tr):
  date_text = tr.find('span', class_='homearticleheader').text[0:10]
  name, url = tr.find('a').text.strip(), tr.find('a')['href']
  permit_id = re.search('permit=([0-9-]+)', url).group(1)
  month, day, year = date_text.split('/')
  date = '%s-%s-%s' % (year, month, day)
  discipline = tr.find('span', title='discipline').text.strip()
  age = tr.find('span', title='age')
  age = age.text.strip() if age else None
  return {'age': age, 'date': date, 'discipline': discipline, 'name': name, 'permit_id': permit_id}


def extract_second_row(tr):
  text = tr.find('td').text.strip()
  if not re.search('^\d+ \/ \d+$', text):
    return None
  place, field = text.split(' / ')
  return {'field': int(field), 'place': int(place)}


def get_comp_id(href):
  maybe_id = re.search('^\/results\/?\?compid=(\d+)$', href)
  return maybe_id.group(1) if maybe_id else None


def member_link(el):
  return el.name == 'a' and el.text.strip() and el.has_attr('href') and get_comp_id(el['href'])


def make_member(a):
  return {'comp_id': get_comp_id(a['href']), 'name': a.text.strip()}


def make_soup(url):
  return bs4.BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')


def result_pair(el):
  if el.name != 'tr':
    return False
  if el.has_attr('bgcolor'):
    return True
  return el.has_attr('class') and 'homearticlebody' in el['class']


def main(args):
  club_url = CLUB_URL_TEMPLATE % args.club_id
  members = map(make_member, make_soup(club_url).find_all(member_link))
  results = []

  if not members:
    print >> sys.stderr, 'No members for that club found'

  for member in members:
    member_url = RESULTS_URL_TEMPLATE % member['comp_id']
    races = make_soup(member_url).find('table').find_all(result_pair)

    # if not races:
    #  print >> sys.stderr, 'No race results found for %s (%s)' % (member['name'], member_url)

    assert len(races) % 2 == 0
    num_races = len(races) / 2

    first_rows = map(extract_first_row, races[0::2])
    second_rows = map(extract_second_row, races[1::2])
    assert len(first_rows) == num_races and len(second_rows) == num_races

    for i in range(0, num_races):
      if not second_rows[i]:
        continue  # DNF
      result = {'member': member}
      result.update(first_rows[i])
      result.update(second_rows[i])
      results.append(result)

  if args.only_current_year:
    current_year = str(datetime.datetime.now().year)
    results = filter(lambda r: r['date'].startswith(current_year), results)

  if args.only_road:
    road_reg = '^(RR|CRIT|ITT|TT|OMNI|GC|CCR|STR)$'
    results = filter(lambda r: re.search(road_reg, r['discipline']), results)

  if args.min_field_size:
    results = filter(lambda r: r['field'] >= args.min_field_size, results)

  if args.min_place:
    results = filter(lambda r: r['place'] <= args.min_place, results)

  if args.sort_by_date:
    results = sorted(results, key=lambda r: r['date'], reverse=True)

  return results


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Scrape a USAC club's results")
  parser.add_argument('club_id', type=int, help='USAC club ID')
  parser.add_argument('--jsonp_callback', type=str, help='A JSONP callback')
  parser.add_argument('--min_field_size', type=int, help='Minimum race field size')
  parser.add_argument('--min_place', type=int, help='Minimum race place')
  parser.add_argument('--only_current_year', type=bool, help='Only show results from current year', default=True)
  parser.add_argument('--only_road', type=bool, help='Only road results')
  parser.add_argument('--sort_by_date', type=bool, help='Sort results reverse chronologically', default=True)
  args = parser.parse_args(sys.argv[1:])
  import json
  results_json = json.dumps(main(args))
  if args.jsonp_callback:
    results_json = args.jsonp_callback + '(' + results_json + ')'
  print results_json
