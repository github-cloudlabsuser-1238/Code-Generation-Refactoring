import requests

# Fetch weather data from OpenWeatherMap API


def fetch_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+",uk&APPID="+api_key

    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
api_key = 'cc9bf689b28589b16a00418368facc37'
city = 'London'
weather_data = fetch_weather(api_key, city)
if weather_data:
    print(weather_data)
else:
    print("Failed to fetch weather data")