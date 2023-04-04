#!/usr/bin/env python3

# TODO: rename to scrape_usac_members.py?

import bs4
import datetime
import json
import os
import random
import re
import sys
import time
import urllib.request


RESULTS_URL_TEMPLATE = 'http://legacy.usacycling.org/results/?compid=%s'


_HERE = os.path.dirname(__file__)

_DEFAULT_MEMBERS_JSON_PATH=os.path.join(_HERE, 'members.json')

_USER_AGENT = open(os.path.join(_HERE, 'user_agent.txt')).read().strip()
_ALL_PROXIES = open(os.path.join(_HERE, 'http_proxy.txt')).read().strip().splitlines()
_HTTP_PROXY = _ALL_PROXIES[random.randint(0, len(_ALL_PROXIES) - 1)].strip()
print('Using HTTP proxy: %s' % _HTTP_PROXY, file=sys.stderr)


_PROXY_HANDLER = urllib.request.ProxyHandler({'http': _HTTP_PROXY})
_URL_OPENER = urllib.request.build_opener(_PROXY_HANDLER)
_URL_OPENER.addheaders = [('User-Agent', _USER_AGENT)]


def extract_first_row(tr):
  date_text = tr.find('span', class_='homearticleheader').text[0:10]
  name, url = tr.find('a').text.strip(), tr.find('a')['href']
  permit_id = re.search('permit=([0-9-]+)', url).group(1)
  month, day, year = date_text.split('/')
  if not year.isdigit() or int(year) < 1900:
    return
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


def make_soup(url):
  start = time.time()
  contents = _URL_OPENER.open(url).read()
  print('Loading %s took %.2f seconds' % (url, time.time() - start), file=sys.stderr)
  return bs4.BeautifulSoup(contents, 'html.parser')


def result_pair(el):
  if el.name != 'tr':
    return False
  if el.has_attr('bgcolor'):
    return True
  return el.has_attr('class') and 'homearticlebody' in el['class']


def main(args):
  members = json.load(open(args.members_json_path))
  results = []

  if not members:
    print('No members for that club found', file=sys.stderr)

  for member in members:
    member_url = RESULTS_URL_TEMPLATE % member['comp_id']
    print('Scraping member: %s (%s)' % (member['name'], member_url), file=sys.stderr)
    races = make_soup(member_url).find('table').find_all(result_pair)

    if not races:
      print('No race results found for %s (%s)' % (member['name'], member_url), file=sys.stderr)

    assert len(races) % 2 == 0
    num_races = int(len(races) / 2)

    first_rows = list(map(extract_first_row, races[0::2]))
    second_rows = list(map(extract_second_row, races[1::2]))
    assert len(first_rows) == num_races and len(second_rows) == num_races

    for i in range(0, num_races):
      if not first_rows[i]:
        continue  # bad date (e.g. 00/00/0000)
      if not second_rows[i]:
        continue  # DNF
      result = {'member': member}
      result.update(first_rows[i])
      result.update(second_rows[i])
      results.append(result)

    time.sleep(4)

  if args.since:
    parse_date = lambda s: datetime.datetime.strptime(s, '%Y-%m-%d')
    since = parse_date(args.since)
    results = filter(lambda r: parse_date(r['date']) > since, results)

  if args.only_road:
    road_reg = '^(RR|CRIT|ITT|TT|OMNI|GC|CCR|STR)$'
    results = filter(lambda r: re.search(road_reg, r['discipline']), results)

  if args.min_field_size:
    results = filter(lambda r: r['field'] >= args.min_field_size, results)

  if args.min_place:
    results = filter(lambda r: r['place'] <= args.min_place, results)

  if args.sort_by_date:
    results = sorted(results, key=lambda r: r['date'] + r['permit_id'], reverse=True)

  return results


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Scrape a list of USAC's competitors' results")
  parser.add_argument('--members_json_path', type=str, help='Path to members JSON file', default=_DEFAULT_MEMBERS_JSON_PATH)
  parser.add_argument('--jsonp_callback', type=str, help='A JSONP callback')
  parser.add_argument('--min_field_size', type=int, help='Minimum race field size')
  parser.add_argument('--min_place', type=int, help='Minimum race place')
  parser.add_argument('--since', type=str, help='Only show results since this date (Y-m-d)', default='%s-01-01' % datetime.datetime.now().year)
  parser.add_argument('--only_road', type=bool, help='Only road results', default=True)
  parser.add_argument('--sort_by_date', type=bool, help='Sort results reverse chronologically', default=True)
  args = parser.parse_args(sys.argv[1:])

  results_json = json.dumps(main(args))
  if args.jsonp_callback:
    results_json = args.jsonp_callback + '(' + results_json + ')'
  print(results_json)
