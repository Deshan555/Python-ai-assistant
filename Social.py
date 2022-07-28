
import Voice_TT

import Human_Names

import webbrowser

import AI_Model


def insta():

    #text = AI_Model.text

    name = Human_Names.name_recognizer(text)

    if name == 'none':

        base_url = "https://www.instagram.com"

    else:
        base_url = "https://www.instagram.com/"+name+"/"

        base_url = base_url.replace(" ", "")

    webbrowser.open(base_url, new=2)


