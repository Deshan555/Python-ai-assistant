import configparser

import random

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

import Speak


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


response: list = ["your name is", "you are", "i know your name"]

donut_know: list = ["i still don't know you so what is your name", "i am still learning please tell me your name", "i don't know but i love to know that, so whats your name"]

got_it: list = ["got it", "ok now i know it", "thank you for help me for learn"]


def name_operations():

    parser = configparser.ConfigParser()

    parser.read("config.ini")

    name = parser.get("config", "user_name")

    if name == "notset_yet":

        Speak.Speak(random.choice(donut_know))

        names = voice_Text().lower()

        if names == 'none':

            names = voice_Text().lower()

        else:

            update_name(names)

    else:
        Speak.Speak(random.choice(response))

        Speak.Speak(name)


def update_name(name):

    edit = configparser.ConfigParser()

    edit.read("config.ini")

    user_section = edit["config"]

    user_section["user_name"] = name

    with open('config.ini', 'w') as configfile:

        edit.write(configfile)

        Speak.Speak(random.choice(got_it))


