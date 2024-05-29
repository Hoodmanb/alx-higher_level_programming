$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format = json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    data.results.forEach(film => {
      console.log(film.title);
      const listItem = $('<li></li>').text(film.title);
      $('#list_movies').append(listItem);
    });
  },
  error: function (jqXHR, textStatus, errorThrown) {
    console.error('Error:', textStatus, errorThrown);
  }
});
