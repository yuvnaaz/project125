from flask import Flask, jsonify, request
from classifier import get_prediction
app = Flast(__name__)

@app.route('/predict-alphabet', methods=['POST'])
def predict_alphabet():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
    return jsonify({
        "prediction": prediction
    }), 200

