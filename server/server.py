from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/api/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.estimated_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print(">>> Running the correct server.py file")
    util.load_saved_artifacts()
    app.run(debug=True)
