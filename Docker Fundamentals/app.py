
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)


# Load model at startup
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Class names for Iris dataset
class_names = ['setosa', 'versicolor', 'virginica']


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "model": "loaded"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # 1. Grab the data sent by the user
    features = np.array(data['features']).reshape(1, -1) # 2. Format it for the model
    
    prediction = model.predict(features)[0] # 3. Get the category (0, 1, or 2)
    probability = model.predict_proba(features)[0].tolist() # 4. Get the confidence scores
    
    return jsonify({ # 5. Send the answer back
        "prediction": int(prediction),
        "class_name": class_names[prediction],
        "probabilities": probability
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)