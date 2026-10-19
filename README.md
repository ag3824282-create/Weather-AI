# Weather AI

Weather AI is a small Python application for looking up current weather by city. It provides both a Flask web interface and an interactive terminal interface. Both use the same weather service, which validates the city, checks a local JSON cache, and requests current conditions from OpenWeather when needed.

## Features

- Search current weather by city in a browser or terminal.
- Show temperature in Celsius, condition description, humidity, and wind speed.
- Cache successful results locally for one hour to reduce repeat API requests.
- Share weather lookup logic between both interfaces.

## Requirements

- Python 3.9 or newer.
- An OpenWeather API key with access to the Current Weather API.
- Internet access for cache misses.

## Setup

From the project directory, create and activate a virtual environment in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for the current terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Configure the API Key

The current application reads `API_KEY` from `config.py`; it does not load the existing `.env` file. Set `API_KEY` to your own OpenWeather key in your local `config.py` before using the app:

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

Do not commit a real API key or share it in screenshots or logs. A real credential is currently present in the project's source configuration, so revoke or rotate that key and avoid reusing it. Environment-variable based secret loading should be added before sharing or deploying the project.

## Run the Web App

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000), enter a city, and submit the form. The current Flask entry point runs with debug mode enabled, which is suitable only for local development.

## Run the Terminal App

```powershell
python terminal_app.py.py
```

Choose **Search weather**, enter a city, and view the result. Choose **Exit** to close the application.

## Cache

Weather results are stored in `data/weather_cache.json`, keyed by normalized city name. Entries are considered fresh for one hour. Expired entries are ignored and fetched again on the next lookup. The cache path is relative to the current working directory, so run the app from the project root.

## Project Structure

```text
app.py                       Flask web entry point
terminal_app.py.py           Terminal entry point
config.py                    API and cache settings
services/weather_service.py  Shared validation and weather lookup
services/weather_cache.py    JSON cache implementation
utils/validators.py          City input validation
utils/menu.py                Terminal menu rendering
templates/index.html         Web page template
static/css/style.css         Web page styles
static/js/script.js          Browser script (currently empty)
data/weather_cache.json      Local weather cache
database/db_setup.py         Standalone SQLite users-table setup
database/db_handler.py       Empty database handler placeholder
tests/                       Test directory (tests are not implemented yet)
```

The SQLite setup is not used by the current weather lookup flow. User accounts and database-backed weather history are not implemented.

## Known Limitations

- Invalid API credentials currently surface through the general provider-error path rather than a dedicated invalid-key message.
- The configured request timeout is not currently passed to the HTTP request.
- The JSON cache is intended for simple local use and does not provide concurrency protection for multiple server workers.
- Automated tests have not yet been implemented.
