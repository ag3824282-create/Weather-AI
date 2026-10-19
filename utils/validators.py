def validate_city(city):
    if not city or not isinstance(city, str):
        raise ValueError("City name must be a non-empty string.")
    if not city.strip():
        raise ValueError("City name cannot be empty or whitespace.")
    return city.strip()