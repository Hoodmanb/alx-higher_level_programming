$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';

  $('form').on('submit', function (e) {
    e.preventDefault();
    const langCode = $('#language_code').val(); // Get the language code here
    $.ajax({
      url: `${url}?lang=${langCode}`,
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        $('#hello').html(data.hello);
        console.log(data.hello);
        console.log(data);
      },
      error: function (error) {
        console.log('Error: ', error);
      }
    });
  });
});
