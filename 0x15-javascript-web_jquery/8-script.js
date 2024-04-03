/* global $ */
$(document).ready(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data) {
      for (let i = 0; i < data.results.length; i++) {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
      }
    }
  );
});
