function post() {

  let name = $('input').value;
  let comment = $('textarea').value;
  let num = document.getElementsByClassName('container post').length;
  if (num % 2 === 0) ? theme = 'even', 'odd';
  $('.container-fluid.post').append(
    '<div class=container post ' + theme
    + '><h2>' + name + '</h2><p>' + comment + '</p></div>'
  );
}
