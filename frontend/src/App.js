import logo from './logo.svg';
import './App.css';
import React from 'react';
import TrainModelForm from './components/TrainModelForm';


function App() {
    return (
        <div className="App">
         <a
          className="App-link"
          href="http://localhost:5000/"
          target="_blank"
          rel="noopener noreferrer"
        >
          MLFLOW UI LINK
        </a>


            <TrainModelForm />
        </div>
    );
}

export default App;
