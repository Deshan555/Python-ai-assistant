import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')

engine.setProperty('rate', 175)


class Speak:

    def __init__(self, message):

        engine.say(message)

        engine.runAndWait()



