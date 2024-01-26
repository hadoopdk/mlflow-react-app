import React, { useState } from 'react';
import axios from 'axios';

const TrainModelForm = () => {
    const [parameters, setParameters] = useState({ n_estimators: '100', max_depth: '4' });  // Initially as strings
    const [trainingResult, setTrainingResult] = useState(null);

    const handleInputChange = (event) => {
        setParameters({ ...parameters, [event.target.name]: event.target.value });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        // Convert form values to integers
        const intParams = {
            n_estimators: parseInt(parameters.n_estimators, 10),
            max_depth: parseInt(parameters.max_depth, 10)
        };

        try {
            const response = await axios.post('http://localhost:8000/train', intParams);
            setTrainingResult(response.data);
        } catch (error) {
            console.error('Error during model training:', error);
        }
    };

    return (
        <div>
            <h2>Train Model</h2> 
            <form onSubmit={handleSubmit}>
                <input 
                    type="number" 
                    name="n_estimators" 
                    value={parameters.n_estimators} 
                    onChange={handleInputChange} 
                />
                <input 
                    type="number" 
                    name="max_depth" 
                    value={parameters.max_depth} 
                    onChange={handleInputChange} 
                />
                <button type="submit">Train</button>
            </form>
            {trainingResult && <div>Accuracy: {trainingResult.accuracy}</div>}
            
        </div>
    );
};

export default TrainModelForm;
