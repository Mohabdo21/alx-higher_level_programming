/* global $ */
$(document).ready(function () {
  function translate () {
    const lang = $('#language_code').val();
    $.get(
      'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      function (data) {
        $('#hello').text(data.hello);
      }
    );
  }

  $('#btn_translate').click(translate);
  $('#language_code').keypress(function (key) {
    if (key.which === 13) {
      translate();
    }
  });
});
