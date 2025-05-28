import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Weather API Flask App!"

@app.route("/weather/<city>")
def get_weather(city):
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        return jsonify({"error": "API key not found in environment variable"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return jsonify({
            "city": city,
            "temperature_celsius": temp,
            "description": weather_desc
        })
    else:
        return jsonify({
            "error": "Failed to fetch weather data",
            "details": response.json()
        }), response.status_code

if __name__ == "__main__":
    # Run Flask app in debug mode (remove debug=True in production)
    app.run(debug=True)
