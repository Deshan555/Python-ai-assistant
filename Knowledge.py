
import Config

import wolframalpha

import Speak

import Voice_TT


def Application_Knowledge(question: str):

    app_id = Config.API_Wolfram

    client = wolframalpha.Client(app_id)

    res = client.query(question)

    answer = next(res.results).text

    try:
        print(answer)
    except:
        pass



while True:

    text = Voice_TT.mic_get()

    print(text)

    if text == 'none':

        Speak.Speak("I didn't get that")

    else:

        Application_Knowledge(text.lower())



