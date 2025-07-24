from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "3c25276d2223bf10a8a31a0c40bf1446"
BASE_URL = "http://api.weatherstack.com/current"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(BASE_URL, params={"access_key": API_KEY, "query": city})
            data = response.json()
            if "current" in data:
                weather_data = {
                    "city": city,
                    "temperature": data["current"]["temperature"],
                    "condition": data["current"]["weather_descriptions"][0]
                }
            else:
                error = "City not found!"
        else:
            error = "Please enter a city name."
    return render_template('index.html', weather=weather_data, error=error)

# Removed app.run() for Vercel serverless compatibility
# The app object is exposed as the WSGI callable for Vercel

# No need to call app.run() in serverless environment
