from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# In-memory database for demonstration
items = [
    {"id": 1, "name": "Sample Item", "description": "This is a sample item"}
]

# Weather API configuration
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Name is required"}), 400
    
    new_item = {
        'id': len(items) + 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    if 'name' in request.json:
        item['name'] = request.json['name']
    if 'description' in request.json:
        item['description'] = request.json['description']
    
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    items = [i for i in items if i['id'] != item_id]
    return jsonify({"result": "Item deleted"})

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    try:
        params = {
            'key': WEATHER_API_KEY,
            'q': city,
            # 'units': 'metric'  # For Celsius, use 'imperial' for Fahrenheit
        }
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        # Extract relevant data
        simplified_data = {
            'city': weather_data['location']['name'],
            'temperature': weather_data['current']['temp_c'],
            'description': weather_data['current']['condition']['text'],
            'humidity': weather_data['current']['humidity'],
            'wind_speed': weather_data['current']['wind_kph']
        }
        return jsonify(simplified_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)