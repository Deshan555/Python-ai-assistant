import webbrowser

import pywhatkit

import wikipedia

import Carbon_Value
import Events

import News

import Screen_Shot

import Send_News
import Send_Weather

import Speak

import datetime

import speech_recognition as sr

import Temperature
import Weather
import music


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        Speak.Speak("Good Morning!")

    elif 12 <= hour < 18:
        Speak.Speak("Good Afternoon!")

    else:
        Speak.Speak("Good Evening!")

    Speak.Speak("I am Tessa . Please tell me , how Can I help you")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return command


if __name__ == "__main__":

    wishMe()

    while True:

        query = takeCommand().lower()

        if 'hay' in query:

            Speak.Speak('Hey How Are You? How Can I Help You')

        elif 'wikipedia' in query:

            Speak.Speak('Searching Wikipedia...')

            query = query.replace("wikipedia", "")

            try:
                results = wikipedia.summary(query, sentences=10)

                Speak.Speak("According to Wikipedia")

                Speak.Speak(results)

            except Exception as e:

                Speak.Speak("Results Not Found")

        elif 'send' in query:

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

            Carbon_Value.event()










