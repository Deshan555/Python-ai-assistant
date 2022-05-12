from pygooglenews import GoogleNews

import Speak


class get_news:

    def __init__(self):

        count: int = 0

        gn = GoogleNews()

        s = gn.search('Sri Lanka')

        for entry in s["entries"]:

            if count < 5:
                Speak.Speak(entry["title"])

            else:
                pass

            count = count + 1
