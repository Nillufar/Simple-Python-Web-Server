from flask import Flask, send_from_directory, jsonify
import random

app = Flask(__name__, static_folder='.')

# Serve the index.html from current folder when user visits "/"
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# API endpoint to provide simulated sensor data as JSON
@app.route('/api/sensor')
def sensor_data():
    data = {
        'temperature': round(20 + random.random() * 10, 1),  # 20.0 to 30.0 °C
        'gas': round(300 + random.random() * 100),          # 300 to 400 ppm (example)
        'activity': random.choice(['Active', 'Inactive'])   # Random activity status
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

