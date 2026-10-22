import React, { useState, useEffect } from 'react';
import './App.css';
import TodoView from './components/TodoListView';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {

  // Store the todo list and form input values.
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');
  
  // Store the active theme state.
  const [isDarkMode, setIsDarkMode] = useState(false);

  // Fetch all todos from the backend and update the list.
  useEffect(() => {
    axios.get('http://localhost:8000/api/todo')
      .then(res => {
        setTodoList(res.data);
      });
  }, []); 

  // Send a new todo to the backend using the form values.
  const addTodoHandler = () => {
    axios.post('http://localhost:8000/api/todo/', {
      'title': title,
      'description': desc
    })
      .then(res => console.log(res));
  };

  // Render the application layout, task form, and todo list.
  return (
    <div 
      className="App list-group-item justify-content-center align-items-center mx-auto" 
      style={{ 
        width: "400px", 
        backgroundColor: isDarkMode ? "#212529" : "white", 
        color: isDarkMode ? "white" : "black",
        marginTop: "15px",
        transition: "background-color 0.3s ease"
      }}
    >
      <button 
        className={`btn btn-sm mb-3 mt-2 ${isDarkMode ? 'btn-light' : 'btn-dark'}`} 
        onClick={() => setIsDarkMode(!isDarkMode)}
      >
        {isDarkMode ? "Light Mode" : "Dark Mode"}
      </button>

      <h1 className="card text-white bg-primary mb-1" style={{ maxWidth: "20rem" }}>Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>

      <div className="card-body">
        <h5 className={`card text-white bg-dark mb-3 ${isDarkMode ? 'border-secondary' : ''}`}>Add Your Task</h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" onChange={event => setTitle(event.target.value)} placeholder="Title" />
          <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)} placeholder="Description" />
          <button className="btn btn-outline-primary mx-2 mb-3" style={{ borderRadius: "50px", fontWeight: "bold" }} onClick={addTodoHandler}>Add Task</button>
        </span>

        <h5 className={`card text-white bg-dark mb-3 ${isDarkMode ? 'border-secondary' : ''}`}>Your Tasks</h5>
        <div>
          <TodoView todoList={todoList} />
        </div>
      </div>

      <h6 className="card text-dark bg-warning py-1 mb-0">Copyright 2021, All rights reserved &copy;</h6>
    </div>
  );
}

export default App;