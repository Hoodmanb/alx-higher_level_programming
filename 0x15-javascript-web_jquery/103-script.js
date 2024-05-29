$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
      return false;
    }
  });

  $('#btn_translate').on('click', function () {
    const langCode = $('#language_code').val();
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
