import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

def load_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    return api_key

def get_lat_lon(city_name, state_code, country_code, api_key):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}").json()
    data = response[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon

def get_current_weather(lat, lon, api_key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric").json()
    data = WeatherData(
        main=response.get("weather")[0].get("main"),
        description=response.get("weather")[0].get("description"),
        icon=response.get("weather")[0].get("icon"),
        temperature=response.get("main").get("temp"),
    )
    return data

def main(city_name, state_code, country_code):
    api_key = load_api_key()
    lat, lon = get_lat_lon(city_name, state_code, country_code, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    print(weather_data)

if __name__ == "__main__":
    city_name = "Toronto"
    state_code = "ON"
    country_code = "CA"
    main(city_name, state_code, country_code)
