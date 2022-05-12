from datetime import date

import requests

import Pushbullet

import Speak

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = "Rathnapura"

API_KEY = "ab46492c5e954d033a7e4a6afe58ccde"


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

            weather_get = weather_report[0]['description']

            today = date.today()

            message = 'Here Today Weather Report In '+CITY+'\n Temperature Feel like : '+str(temperature)+'K\n Weather Feel Like : '+str(temp_feel_like)+'K\n Humidity : '+str(humidity)+'%\n Air Pressure : '+\
                      str(pressure)+'Kelvin\n Wind Report : '+str(wind_report)+'Km/h\n Overall Weather Like : '+weather_get

            Pushbullet.Push_bullet('Weather Report Today '+str(today), message)

            Speak.Speak("Weather Report Sent To Your Device")

        else:

            Speak.Speak("Error in the HTTP request")
