// login.js
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    if (!username || !password) {
      alert('Por favor, ingresa tu usuario y contraseña.');
    } else {
      // Aquí puedes enviar el formulario al servidor o realizar alguna otra acción.
      // Puedes modificar esta parte según tus necesidades.
      document.getElementById('login-form').submit();
    }
  });
  