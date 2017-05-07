showlogin = function() {
  a = document.getElementById('errorlogin');
  x = document.getElementsByClassName('login-section');
  y = document.getElementsByClassName('signup-section');
  z = document.getElementsByClassName('triggered');
  if (a.innerText !== "") {
    x[0].style.display = 'block';
    y[0].style.display = 'none';
    z[0].innerText = 'Sign up'
  }
}

login = function() {
  x = document.getElementsByClassName('login-section');
  y = document.getElementsByClassName('signup-section');
  z = document.getElementsByClassName('triggered');
  if (x[0].style.display === 'none') {
    x[0].style.display = 'block';
    y[0].style.display = 'none';
    z[0].innerText = 'Sign up'
  } else {
    x[0].style.display = 'none';
    y[0].style.display = 'block';
    z[0].innerText = 'Log in'
  }
};
