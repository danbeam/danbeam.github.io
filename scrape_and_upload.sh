#!/bin/bash

set -e

readonly HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="$HERE/race_results.log"

log() {
  echo "`date`: $@" >> "$LOG_FILE"
}

log "I woke up"

readonly SCRAPE_CMD="python $HERE/scrape_usac_club.py"
readonly CLUB_ID=15733
readonly EXTRA_ARGS="--jsonp_callback got_race_results"

readonly TMP_FILE="$HERE/got_race_results.js.tmp"
readonly RESULTS_FILE="$HERE/got_race_results.js"

log "scraping USAC"
eval "$SCRAPE_CMD $CLUB_ID $EXTRA_ARGS" > "$TMP_FILE"
log "done scraping USAC"

readonly DIFF_RESULTS=$(diff "$RESULTS_FILE" "$TMP_FILE")

if [[ -z "$DIFF_RESULTS" ]]; then
  log "same results"
  rm "$TMP_FILE"
else
  /bin/mv "$TMP_FILE" "$RESULTS_FILE"
  log "new results"
  git add "$RESULTS_FILE"
  git commit -q -m 'new results'
  { eval `ssh-agent`; ssh-add race_results.rsa; } &>/dev/null
  git push -q origin master
  { eval `ssh-agent -k`; } &>/dev/null
fi

log "going back to bed"
