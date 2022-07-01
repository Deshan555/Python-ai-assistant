
import Config

import random

import wolframalpha

import Speak

Respond: list = ["math solver did not support voice Input Please type your question on console", "Voice inputs not allow to that function, please type your question on console", "for provide correct answer please type your question", ]

Respond_open: list = ["okay sure", "why not lets do it", "at your service"]


def Application_Knowledge(question: str):

    try:
        app_id = Config.API_Wolfram

        client = wolframalpha.Client(app_id)

        res = client.query(question)

        answer = next(res.results).text

        print('Answer = ', answer)

        Speak.Speak('Your Answer ')

        Speak.Speak(answer)

    except:
        pass


def Running_Math():

    Speak.Speak(random.choice(Respond_open))

    Speak.Speak(random.choice(Respond))

    Question = input("Question : ")

    Application_Knowledge(Question)



