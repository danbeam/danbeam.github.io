#!/bin/bash

set -e

readonly HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="$HERE/race_results.log"

log() {
  echo "`date`: $@" >> "$LOG_FILE"
}

readonly SCRAPE_CMD="python $HERE/scrape_usac_club.py"
readonly CLUB_ID=15733
readonly EXTRA_ARGS="--jsonp_callback got_race_results"

readonly TMP_FILE="$HERE/got_race_results.js.tmp"
readonly RESULTS_FILE="$HERE/got_race_results.js"

eval "$SCRAPE_CMD $CLUB_ID $EXTRA_ARGS" > "$TMP_FILE"

readonly DIFF_RESULTS=$(diff "$RESULTS_FILE" "$TMP_FILE")

if [ -z "$DIFF_RESULTS" ] && [ "$@" != "-f" ]; then
  log "same results"
  rm "$TMP_FILE"
else
  /bin/mv "$TMP_FILE" "$RESULTS_FILE"
  log "got new results"
  git add "$RESULTS_FILE"
  git commit -m 'new results'
  eval `ssh-agent`
  ssh-add race_results.rsa
  git push origin master
  eval `ssh-agent -k`
fi
