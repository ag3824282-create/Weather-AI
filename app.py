from services.weather_service import search_weather
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    try:
        weather_info = search_weather(city)
        
        return render_template("index.html", weather=weather_info)
    except (ValueError, ConnectionError) as exc:
        return render_template("index.html", error = str(exc))

if __name__ == '__main__':
    app.run(debug=True)
