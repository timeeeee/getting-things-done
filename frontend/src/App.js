import React, {useState, useEffect} from 'react';
import axios from 'axios';

import './App.css';

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
*/

function App() {
    const [value, setValue] = useState('*loading*');
    
    useEffect(() => {
        axios.get('http://localhost:8000/')
	    .then(function (response) {
		// handle success
		console.log(response);
		setValue(response.data['Hello']);
	    })
	    .catch(function (error) {
		// handle error
		console.log(error);
	    })
	    .finally(function () {
		// always executed
	    });
    }, []);
    
    return (
        <p>Hello, {value}</p>
    );
}

export default App;
