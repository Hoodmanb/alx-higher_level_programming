$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      console.log(data.hello);
      $('#hello').text(data.hello);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('Error:', textStatus, errorThrown);
    }
  });
});
