login = function() {
  x = document.getElementsByClassName('login-section');
  y = document.getElementsByClassName('signup-section');
  if (x[0].style.display === 'none') {
    x[0].style.display = 'block';
    y[0].style.display = 'none';
  } else {
    x[0].style.display = 'none';
    y[0].style.display = 'none';
  }
};

signup = function() {
  x = document.getElementsByClassName('signup-section');
  y = document.getElementsByClassName('login-section');
  if (x[0].style.display === 'none') {
    x[0].style.display = 'block';
    y[0].style.display = 'none';
  } else {
    x[0].style.display = 'none';
    y[0].style.display = 'none';
  }
};
