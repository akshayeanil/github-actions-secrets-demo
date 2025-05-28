import os
import requests

def main():
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        print("ERROR: No API key found in WEATHER_API_KEY environment variable.")
        exit(1)

    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        print(f"The temperature in {city} is {temp}°C")
    else:
        print(f"Failed to get weather data: {response.status_code} - {response.text}")
        exit(1)

if __name__ == "__main__":
    main()
