import bs4
import urllib
import re


BASE_URL = 'https://legacy.usacycling.org'
CLUB_ID = '15733'
PREV_MEMBERS = ['405697']
RESULTS_URL = BASE_URL + '/results/'
TEAM_URL = BASE_URL + '/clubs/members.php?club=' + CLUB_ID


def get_comp_id(href):
  maybe_id = re.search('^\/results\/?\?compid=(\d+)$', href)
  return maybe_id.group(1) if maybe_id else None


def make_member(a):
  return {'comp_id': get_comp_id(a['href']), 'name': a.text.strip()}


def make_soup(url):
  return bs4.BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')


def member_link(el):
  if el.name != 'a' or not el.text.strip() or not el.has_attr('href'):
    return False
  comp_id = get_comp_id(el['href'])
  return comp_id and not comp_id in PREV_MEMBERS


members = map(make_member, make_soup(TEAM_URL).find_all(member_link))
assert members


def result_pair(el):
  if el.name != 'tr':
    return False
  if el.has_attr('bgcolor'):
    return True
  return el.has_attr('class') and 'homearticlebody' in el['class']


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


results = []

for member in members:
  member_url = RESULTS_URL + '?compid=' + member['comp_id']
  races = make_soup(member_url).find('table').find_all(result_pair)
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

good_results = filter(lambda r: r['field'] > 10 and r['place'] < 10, results)
recent_results = sorted(good_results, key=lambda r: r['date'], reverse=True)

print recent_results[0:10]  # TODO: better output ;)