window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const leng = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
    console.log(url);
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};
