import requests

import Config

import Speak

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = Config.BASE_CITY

API_KEY = Config.AUTH_KEY


class get_Weather:

    def __init__(self):

        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

        response = requests.get(URL)

        if response.status_code == 200:

            data = response.json()

            main = data['main']

            temperature = main['temp']

            temp_feel_like = main['feels_like']

            humidity = main['humidity']

            pressure = main['pressure']

            weather_report = data['weather']

            wind_report = data['wind']

            Speak.Speak('Here Today Weather Report In '+CITY)

            Speak.Speak(f" Today Weather Like {weather_report[0]['description']}")

            Speak.Speak(f"Temperature: {temperature} in Kelvin")

            Speak.Speak(f"Feel Like: {temp_feel_like} in Kelvin")

            Speak.Speak(f"Humidity: {humidity} Parentage")

            Speak.Speak(f"Pressure: {pressure} in pascal")

            Speak.Speak(f"Wind Speed: {wind_report['speed']} kilometre per hour")

        else:

            Speak.Speak("Error in the HTTP request")
