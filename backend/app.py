from flask import Flask, jsonify, request
import mlflow
import os
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and methods

# Assuming you have a function to train your model in a separate script
sys.path.append('ml_training')
import train_model  # This is a hypothetical script we'll create next

@app.route('/train', methods=['POST'])
def train():
    # Extract parameters from the request
    params = request.get_json()
    
    # Call the ML training function
    result = train_model.run_training(params)

    # Return the result
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    return "Service is up and running", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
