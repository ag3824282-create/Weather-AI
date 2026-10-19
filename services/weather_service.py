import requests
from utils.validators import validate_city
from config import API_KEY, BASE_URL, DEFAULT_UNIT
from services.weather_cache import save_to_cache, get_cached_weather

def build_url(city):
    url = f"{BASE_URL}?q={city}&units={DEFAULT_UNIT}&appid={API_KEY}"
    return url

def fetch_weather(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise

def extract_weather_data(data):
    try:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    except KeyError as e:
        raise KeyError(f"Missing expected data in response: {e}")   

def search_weather(city):
    city = city.strip().lower()
    if not validate_city(city):
        raise ValueError("Invalid city name. Please enter a valid city.")
    
    cached_weather = get_cached_weather(city)
    if cached_weather is not None:
        return cached_weather

    url = build_url(city)
    try:
        data = fetch_weather(url)
        weather_data = extract_weather_data(data)
        save_to_cache(city, weather_data)
        return weather_data
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch weather data: {e}")
    except KeyError as e:
        raise ValueError(f"Invalid response data: {e}")