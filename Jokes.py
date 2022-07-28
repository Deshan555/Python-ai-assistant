
import pyjokes

import Speak


def joke_function():

    get_joke = pyjokes.get_joke(language="en", category="neutral")

    Speak.Speak(get_joke)




