import bs4
import re
import sys
import urllib


BASE_URL = 'https://legacy.usacycling.org'
CLUB_URL_TEMPLATE = BASE_URL + '/clubs/members.php?club=%s'
RESULTS_URL_TEMPLATE = BASE_URL + '/results/?compid=%s'


def date_name_permit(tr):
  date = tr.find('span', class_='homearticleheader').text[0:10]
  name, url = tr.find('a').text.strip(), tr.find('a')['href']
  permit_id = re.search('permit=([0-9-]+)', url).group(1)
  month, day, year = date.split('/')
  sortable_date = '%s-%s-%s' % (year, month, day)
  return {'date': sortable_date, 'name': name, 'permit_id': permit_id}


def field_place(tr):
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

    if not races:
      print >> sys.stderr, 'No race results found for %s (%s)' % (member['name'], member_url)

    assert len(races) % 2 == 0
    num_races = len(races) / 2

    date_name_permits = map(date_name_permit, races[0::2])
    field_places = map(field_place, races[1::2])
    assert len(date_name_permits) == num_races and len(field_places) == num_races

    for i in range(0, num_races):
      if field_places[i]:
        result = {'member': member}
        result.update(date_name_permits[i])
        result.update(field_places[i])
        results.append(result)

  if args.min_field_size:
    results = filter(lambda r: r['field'] >= args.min_field_size, results)

  if args.min_place:
    results = filter(lambda r: r['place'] >= args.min_place, results)

  if args.sort_by_date:
    results = sorted(results, key=lambda r: r['date'], reverse=True)

  if args.max_results:
    results = results[0:args.max_results]

  return results


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Scrape a USAC club's results")
  parser.add_argument('club_id', type=int, help='USAC club ID')
  parser.add_argument('--max_results', type=int, help='Maxium number of results to show', default=10)
  parser.add_argument('--min_field_size', type=int, help='Minimum race field size', default=11)
  parser.add_argument('--min_place', type=int, help='Minimum race place', default=10)
  parser.add_argument('--sort_by_date', type=bool, help='Sort results reverse chronologically', default=True)
  import json
  print json.dumps(main(parser.parse_args(sys.argv[1:])))
