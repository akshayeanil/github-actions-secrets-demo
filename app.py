from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <form action="/weather" method="get">
            <input name="city" placeholder="Enter city name" required>
            <button type="submit">Get Weather</button>
        </form>
    '''

@app.route("/weather")
def weather():
    city = request.args.get("city")
    api_key = os.getenv("WEATHER_API_KEY")

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    
    if response.status_code != 200:
        return f"Error: {response.json().get('message')}"

    data = response.json()
    return f"Weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"

if __name__ == "__main__":
    app.run(debug=True)
