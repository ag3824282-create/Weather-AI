import json
import time
from config import CACHE_FILE, CACHE_TTL


def load_cache():
    try:
        with open(CACHE_FILE, 'r',encoding = "utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_cache(cache_data):
    with open(CACHE_FILE, 'w',encoding = "utf-8") as f:
        json.dump(cache_data,f, indent=4)

def save_to_cache(city,weather_data):
    cache_data = load_cache()
    
    cache_Key = city.lower().strip()
    
    cache_data[cache_Key] = {
        "weather": weather_data,
        "timestamp": time.time()
    }
    save_cache(cache_data)
    
def get_cached_weather(city):
    cache_data = load_cache()
    
    cache_Key = city.lower().strip()

    if cache_Key in cache_data:
        cached_entry = cache_data[cache_Key]
        if time.time() - cached_entry["timestamp"] < CACHE_TTL:
            return cached_entry["weather"]
    return None


