from pygooglenews import GoogleNews

import Pushbullet

import Speak


class send_news:

    def __init__(self):
        gn = GoogleNews()

        s = gn.search('Sri Lanka')

        for entry in s["entries"]:

            Pushbullet.Push_bullet('News Requests', entry["title"])

            Speak.Speak('News Send To Your Device')
