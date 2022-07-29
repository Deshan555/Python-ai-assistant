import datetime

import Speak


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:

        Speak.Speak("Good Morning!")

    elif 12 <= hour < 18:

        Speak.Speak("Good Afternoon!")

    else:

        Speak.Speak("Good Evening!")

    Speak.Speak("Hi I am Luna. Please tell me ,how Can I help you")





