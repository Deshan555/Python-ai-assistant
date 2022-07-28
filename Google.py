import pywhatkit

import Speak

import random

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError


suggestions: list = ["what are you looking for?", "what are you search?", "tell me about your interest", "hey tell me what are you looking for i can search for you"]

response: list = ["okay i got it", "give me couple of seconds", "okay i will search", "ha ha i almost there", "hold on i almost there"]

error: list = ["oh! snap", "that crazy interest slower than my grandma", "oh! sorry problem here", "i can't reach there"]


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


class search_it:

    def __init__(self):

        Speak.Speak(random.choice(suggestions))

        query = voice_Text().lower()

        Speak.Speak(random.choice(response))

        try:

            pywhatkit.search(query)

        except:

            Speak.Speak(random.choice(error))

            pass


