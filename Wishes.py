import datetime

import random

import Speak

import Events

strTime = datetime.datetime.now().strftime('%I:%M %p')


def Good_Morning():

    Speak.Speak(f"Good morning. It's {strTime} Here and")

    Events.event()


def Good_Afternoon():

    Speak.Speak(f"Good Afternoon! It's {strTime} Here now so whats going on")


def Good_Evening():

    Speak.Speak("")


def Knock():

    wish_list: list = ["Knock knock. Who's there? Ash. Ash who? Bless you!",
                       "Knock knock. Who's there? Opportunity. Don't be silly, opportunity doesn't knock twice.",
                       "Knock knock. Who's there? Figs. Figs who? Figs the doorbell, it's broken!"
                       "Knock knock. Who's there? Spell. Spell who? W-H-O."
                       "Knock knock. Who's there? Boo. Boo who? Oh, don't cry, it's only a joke."]

    Speak.Speak(random.choice(wish_list))
