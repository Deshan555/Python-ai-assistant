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

    Speak.Speak(f"Good Evening! It's {strTime} Here now so whats going on")


def bye_bye():

    greeting_list: list = ["Peace or peace out", "Later", "Goodbye", "Bye", "Catch you later", "See you later", "After awhile crocodile", "Be good",
                           "All the best", "Farewell", "Good day", "Hasta la vista", "Take care", "Bye for now", "Take it easy", "Until next time",
                           "Have a good day", "Have a good one"]

    Speak.Speak(random.choice(greeting_list))


def Knock():

    wish_list: list = ["Knock knock. Who's there? Ash. Ash who? Bless you!",
                       "Knock knock. Who's there? Opportunity. Don't be silly, opportunity doesn't knock twice.",
                       "Knock knock. Who's there? Figs. Figs who? Figs the doorbell, it's broken!"
                       "Knock knock. Who's there? Spell. Spell who? W-H-O."
                       "Knock knock. Who's there? Boo. Boo who? Oh, don't cry, it's only a joke."]

    Speak.Speak(random.choice(wish_list))


def you_areWelcome():

    welcome: list = ["I got it", "Don’t mention it", "No worries", "Not a problem", "My pleasure", "It was nothing", "I’m happy to help",
                     "Not at all", "Sure", "Anytime"]

    Speak.Speak(random.choice(welcome))


def who_am_i():

    Speak.Speak("i am Luna and i conversational, voice-activated digital assistant created by Iceberg group "
                "that can perform actions on behalf of a user and provide contextual information.")

    print("i am Luna and i conversational, voice-activated digital assistant created by Iceberg group "
          "that can perform actions on behalf of a user and provide contextual information.")


def Hey_user():

    wish_list: list = ["Hello!", "Hello, what can I do for you?", "hey", "so tell me"]

    Speak.Speak(random.choice(wish_list))

