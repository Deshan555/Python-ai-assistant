
import pywhatkit

import Speak

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

import random


suggestions: list = ["i waiting for your command", "what are you looking for?", "what are you search?", "tell me about your interest", "hey tell me what are you looking for i can search for you", "tell me i will youtube for you"]

response: list = ["i looking for best choices", "hold on", "i working on it", "FRIDAY search for you", "enjoy it", "here we go.."]

error: list = ["oh! i can't find anything", "that crazy interest slower than my grandma", "oh! sorry problem here", "i can't reach there"]


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


class py_youtube:

    def __init__(self):

        Speak.Speak(random.choice(suggestions))

        query = voice_Text().lower()

        Speak.Speak(random.choice(response))

        try:
            pywhatkit.playonyt(query)

        except:

            Speak.Speak(random.choice(error))

            pass