window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const leng = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === '13') {
      const leng = $('INPUT#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
      $.get(url, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
};
