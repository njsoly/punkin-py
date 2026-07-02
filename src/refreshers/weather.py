import json
import requests


def get_weather(api_key, city):
  base_url = "http://api.weatherapi.com/v1/forecast.json"
  params = {
    "key": api_key,
    "q": city,
    "days": 1  # Fetch forecast for today
  }
  response = requests.get(base_url, params = params)
  data = response.json()
  return data


api_key = "35ccc99af17344cf9ee171845260107"
city = "Fridley"
weather_data = get_weather(api_key, city)
print(json.dumps(weather_data, indent=2))
