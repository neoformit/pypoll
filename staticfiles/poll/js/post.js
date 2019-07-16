function updateThemes() {
  let posts = document.getElementsByClassName('container post');
  for (i=0; i < posts.length; i++) {
    let theme = (i % 2 === 0) ? 'even' : 'odd';
    posts[i].classList.add(theme);
  }
}
