document.getElementById('loginForm').addEventListener('submit', function(e){
      e.preventDefault();
      // static demo: redirect to homepage
      window.location.href = '../home/facebook_homepage_layout.html';
    });

document.getElementById('signupForm').addEventListener('submit', function(e){
      e.preventDefault();
      // static demo: after signup, go to login
      window.location.href = 'login.html';
    });
