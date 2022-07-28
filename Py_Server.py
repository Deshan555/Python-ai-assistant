
from neuralintents import GenericAssistant

import speech_recognition as sr

import Speak

def print_hey():

    Speak.Speak("hello luna test run success")


def mic_get():

    audio_Input = sr.Recognizer()

    with sr.Microphone() as source:

        audio_Input.adjust_for_ambient_noise(source, duration=0.2)

        print("Say something: ")

        audio = audio_Input.listen(source)

        try:
            respond = audio_Input.recognize_google(audio, language='en-US')

            print("You said: " + respond)

            return respond

        except:

            print("Speech not recognised")

            return 'none'



mappings = {'hello_luna': print_hey}

Assistant = GenericAssistant('talking_pattern.json', intent_methods=mappings)

Assistant.train_model()

#Assistant.save_model()

#Assistant.load_model()


while True:

    text = mic_get()

    Assistant.request(text)



