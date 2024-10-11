import React from "react"
import {BrowerRouter as Router, Route, Routes} from 'react-router-dom'
import Login from "./LoginPage/Login"
import Register from "./RegisterPage/Register"

function App() {
  return (
    <Router>
      <div className="App">
          <Routes>
            <Route path="/login" component={Login}/>
            <Route path="/register" component={Register}/>
            <Route path="/" element={<h1>CoreChat</h1>}/>
          </Routes>
      </div> 
    </Router>
  );
}

export default App
