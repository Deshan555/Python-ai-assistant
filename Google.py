import Voice_TT

import pywhatkit

import Speak

import random

suggestions: list = ["what are you looking for?", "what are you search?", "tell me about your interest", "hey tell me what are you looking for i can search for you"]

response: list = ["okay i got it", "give me couple of seconds", "okay i will search", "ha ha i almost there", "hold on i almost there"]

error: list = ["oh! snap", "that crazy interest slower than my grandma", "oh! sorry problem here", "i can't reach there"]


class search_it:

    def __init__(self):

        Speak.Speak(random.choice(suggestions))

        query = Voice_TT.mic_get().lower()

        Speak.Speak(random.choice(response))

        try:

            pywhatkit.search(query)

        except:

            Speak.Speak(random.choice(error))

            pass


