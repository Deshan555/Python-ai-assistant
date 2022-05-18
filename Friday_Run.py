from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

import os
import webbrowser
import pywhatkit

import wikipedia

import Carbon_Value

import Events

import Humidity

import News

import Request_web

import Screen_Shot

import Send_News

import Send_Weather

import Speak

import datetime

import speech_recognition as sr

import Temperature

import Weather

import Wishes

import music


def voice_Text():

    recognition = Recognizer()

    mic = Microphone()

    with mic:

        recognition.adjust_for_ambient_noise(mic, duration=5)

        print("Talk")

        audio = recognition.record(mic, 7)

    try:
        recognized = recognition.recognize_google(audio)

        print('You Said : ', recognized)

        return recognized

    except UnknownValueError:

        print('Unable to Recognize audio')

        return 'None'

    except RequestError as error:

        print('Error Detected : ', error)

        return 'None'

    return recognized


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:

        Speak.Speak("Good Morning!")

    elif 12 <= hour < 18:

        Speak.Speak("Good Afternoon!")

    else:

        Speak.Speak("Good Evening!")

    Speak.Speak("I am  FRIDAY. . Please tell me , how Can I help you")


if __name__ == "__main__":

    wishMe()

    while True:

        query = voice_Text().lower()

        if 'hay' in query:

            Speak.Speak('Hey How Are You? How Can I Help You')

        elif 'hello friday' in query:

            Speak.Speak('Your Friday here, So tell me what can i do for you')

        elif 'good morning' in query:

            Wishes.wish_toFriday()

        elif 'wikipedia' in query:

            Speak.Speak('Searching Wikipedia...')

            query = query.replace("wikipedia", "")

            try:
                results = wikipedia.summary(query, sentences=10)

                Speak.Speak("According to Wikipedia")

                Speak.Speak(results)

            except Exception as e:

                Speak.Speak("Results Not Found")

        elif 'news send' in query:

            Send_News.send_news()

        elif 'news' in query:

            News.get_news()

        elif 'events' in query:

            Events.event()

        elif 'search for' in query:

            query = query.replace('search for', '')

            pywhatkit.search(query)

        elif 'play' in query:

            query = query.replace('play', '')

            Speak.Speak(query + 'Play soon enjoy music')

            pywhatkit.playonyt(query)

        elif 'quick shot' in query:

            Speak.Speak('Wait Five Seconds For ScreenShot capture')

            Screen_Shot.screen_shot()

        elif 'sing' in query:

            music.music_picker()

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime('%I:%M %p')

            Speak.Speak(f"Sir, the time is {strTime}")

        elif 'weather report' in query:

            Speak.Speak("Please wait I working on it")

            Send_Weather.get_Weather()

        elif 'weather' in query:

            Speak.Speak("Please wait for  get weather details")

            Weather.get_Weather()

        elif 'temperature' in query:

            Temperature.event()

        elif 'carbon value' in query:

            Carbon_Value.event()

        elif 'humidity' in query:

            Humidity.event();

        elif 'turn on pump' in query:

            Speak.Speak('Water Pump Will turn on')

            Request_web.web_requests('http://192.168.43.178/1/on', 'Water Pump turn on successfully')

        elif 'turn off pump' in query:

            Speak.Speak('Water Pump Will turn off')

            Request_web.web_requests('http://192.168.43.178/1/off', 'Water Pump turn off successfully')

        elif 'turn on sprinkler' in query:

            Speak.Speak('sprinkler Will turn on')

            Request_web.web_requests('http://192.168.43.178/2/on', 'sprinkler turn on successfully')

        elif 'turn off sprinkler' in query:

            Speak.Speak('sprinkler Will turn off')

            Request_web.web_requests('http://192.168.43.178/2/off', 'sprinkler turn off successfully')

        elif 'close chrome' in query:

            os.system("taskkill /im chrome.exe /f")

            Speak.Speak('As Your Wish Sir, Chrome Google was close immediately')

