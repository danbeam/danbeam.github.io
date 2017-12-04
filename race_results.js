(function(window) {

var loaded = /interactive|complete/.test(document.readyState);
var results;

window.got_race_results = function(list) { results = list; tryReady(); };

if (!loaded)
  window.addEventListener('load', function() {loaded = true; tryReady(); });

function formatDate(sqlDate) {
  var date = new Date(sqlDate);
  var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return months[date.getMonth()] + ' ' + date.getDate();
}

function formatPlace(place) {
  if (place % 10 == 1 && place != 11)
    return place + 'st';
  if (place % 10 == 2 && place != 12)
    return place + 'nd';
  if (place %10 == 3 && place != 13)
    return place + 'rd';
  return place + 'th';
}

function tryReady() {
  if (!loaded || !results || !results.length)
    return;

  var resultsEl = window.document.querySelector('#block-039956242ae051b42fa7');
  if (!resultsEl) {
    return;
  }

  resultsEl.className += ' results';

  var BASE_URL = 'https://legacy.usacycling.org'
  var MEMBER_BASE = BASE_URL + '/results/?compid=';
  var PERMIT_BASE = BASE_URL + '/results/?permit=';

  for (var i = 0; i < results.length; ++i) {
    var result = results[i];

    var place = document.createElement('b');
    place.className = 'place';
    place.textContent = place.innerText = formatPlace(result.place);

    var rider = document.createElement('a');
    rider.className = 'rider';
    rider.textContent = rider.innerText = result.member.name;
    rider.href = MEMBER_BASE + result.member.comp_id;
    rider.target = '_blank';

    var race = document.createElement('a');
    race.className = 'race';
    var raceName = result.name + ' (' + result.discipline;
    if (result.age && !/open/i.test(result.age))
      raceName += ', ' + result.age;
    raceName += ')';
    race.textContent = race.innerText = raceName;
    race.href = PERMIT_BASE + result.permit_id;
    race.target = '_blank';

    var riderAndRace = document.createElement('div');
    riderAndRace.className = 'rider-and-race';
    riderAndRace.appendChild(rider);
    riderAndRace.appendChild(race);

    var date = document.createElement('span');
    date.className = 'date';
    date.textContent = date.innerText = formatDate(result.date);

    var resultEl = document.createElement('div');
    resultEl.className = 'result';
    resultEl.appendChild(place);
    resultEl.appendChild(riderAndRace);
    resultEl.appendChild(date);

    resultsEl.appendChild(resultEl);
  }
}

}(this));
