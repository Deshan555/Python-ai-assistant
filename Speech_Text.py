
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

from time import sleep


def callback(recognizer, source):

    try:
        recognized = recognizer.recognize_google(source)

        print('You Said : ', recognized)

    except UnknownValueError:

        print('Unable to Recognize audio')

    except RequestError as error:

        print('Error Detected : ', error)


def listen():

    recognition = Recognizer()

    mic = Microphone()

    with mic:

        recognition.adjust_for_ambient_noise(mic)

    print("Talk")

    audio_stopper = recognition.listen_in_background(mic, callback)







