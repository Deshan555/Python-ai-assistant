import datetime

import pywhatkit

import Speak


class screen_shot:

    def __init__(self):

        Speak.Speak('Wait Five Seconds For ScreenShot capture')

        file_name = datetime.datetime.now().strftime('%H:%M %S')+'.JPG'

        delay = 5

        pywhatkit.take_screenshot(file_name, delay)

        print('Process Complete')


