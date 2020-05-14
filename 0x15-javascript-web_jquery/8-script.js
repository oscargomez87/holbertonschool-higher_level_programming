$.ajax({
  type: 'get',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (films) {
    $.each(films.results, function (key, film) {
      $('ul#list_movies').append('<il>' + film.title + '</il>');
    });
  }
});
