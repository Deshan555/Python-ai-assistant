import os

import random

from playsound import playsound

from pathlib import Path

import Speak

FOLDER_PATH = r'C:\Users\Jayashanka Deshan\Music\Fav Music'

abs_list = []


class music_picker:

    def __init__(self):

        fileNames = os.listdir(FOLDER_PATH)

        for fileName in fileNames:

            abs_list.append(os.path.abspath(os.path.join(FOLDER_PATH, fileName)))

        Speak.Speak('Wait I Looking For Best Choices')

        file_path = Path(random.choice(abs_list))

        try:
            playsound(file_path)
        except:
            pass







