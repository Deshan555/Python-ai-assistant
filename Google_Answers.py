import requests

import bs4

import Speak

import random

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

respond: list = ["According my knowledge", "Google said", "Best answer for your question is"]


def voice_Text():

    recognition = Recognizer()

    mic = Microphone()

    with mic:

        recognition.adjust_for_ambient_noise(mic, duration=0.2)

        print("Talk")

        audio = recognition.record(mic, 5)

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


while True:

    Speak.Speak("What Is Your Question? I can help you find answers")

    query = voice_Text().lower()

    url = "https://www.google.com/search?q=" + query.replace(" ", "+")

    request_result = requests.get(url)

    soup = bs4.BeautifulSoup(request_result.text, "html.parser")

    # The answer is stored inside the class "BNeawe".

    temp = soup.find("div", class_='BNeawe').text

    Speak.Speak(random.choice(respond)+temp)

    print(temp)



