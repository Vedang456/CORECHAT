import React, { useState } from 'react';
import './Login.css'; // Import the CSS file

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username === '') {
      alert('Username must be filled out');
      return;
    }
    if (password === '') {
      alert('Password must be filled out');
      return;
    }
    console.log('Login attempt:', { username, password });
    // Here you would typically handle the login logic
  };

  return (
    <div className="Login">
      <h1>Login</h1>
      <form className="Login-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <a href="/register">Register here!</a></p>
    </div>
  );
}

export default Login;