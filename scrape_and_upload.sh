#!/bin/bash

set -e

readonly HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="$HERE/race_results.log"

log() {
  echo "`date`: $@" >> "$LOG_FILE"
}

log "I woke up"

readonly SCRAPE_CMD="python3 $HERE/scrape_usac_club.py"
readonly CLUB_ID=15733
readonly EXTRA_ARGS="--jsonp_callback got_race_results --exclude_comp_ids 549978,22423,188907 --since=2018-01-01"

readonly RESULTS_FILE="$HERE/got_race_results.js"
readonly TMP_FILE="$RESULTS_FILE.tmp"

log "scraping USAC"
eval "$SCRAPE_CMD $CLUB_ID $EXTRA_ARGS" 1>"$TMP_FILE" 2>>"$LOG_FILE"
log "done scraping USAC"

readonly DIFF_RESULTS=$(diff "$RESULTS_FILE" "$TMP_FILE")
if [[ -z "$DIFF_RESULTS" ]]; then
  log "same results"
  rm "$TMP_FILE"
else
  /bin/mv "$TMP_FILE" "$RESULTS_FILE"
  log "new results"
  pushd "$HERE" >/dev/null
  git add "$RESULTS_FILE"
  git commit -q -m 'new results'
  eval `ssh-agent` >/dev/null
  ssh-add race_results.rsa >/dev/null 2>&1
  git push -f -q origin master
  popd >/dev/null
  eval `ssh-agent -k` >/dev/null
fi

log "going back to bed"
