from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/temperature", methods=["POST"])
def temperature():
    data = request.get_json()
    print("Temperature Data:", data)
    return jsonify({"status": "success", "received": data}), 200

@app.route("/api/gas", methods=["POST"])
def gas():
    data = request.get_json()
    print("Gas Data:", data)
    return jsonify({"status": "success", "received": data}), 200

@app.route("/api/humidity", methods=["POST"])
def humidity():
    data = request.get_json()
    print("Humidity Data:", data)
    return jsonify({"status": "success", "received": data}), 200

@app.route("/api/activity", methods=["POST"])
def activity():
    data = request.get_json()
    print("Activity Data:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)
