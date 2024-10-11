import React, { useState } from 'react';
import './Register.css'; // Import the existing CSS file

function Register() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would typically handle the registration logic
    console.log('Registration attempt:', { firstName, lastName, username, password, email });
    // For now, we'll just redirect to the interface page
    window.location.href = '/interface';
  };

  return (
    <div className="Register">
      <h1>Register</h1>
      <form className="Register-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Firstname"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Lastname"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
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
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit">Register</button>
      </form>
      <p>Already have an account? <a href="/login">Login here!</a></p>
    </div>
  );
}

export default Register;