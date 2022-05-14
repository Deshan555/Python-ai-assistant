import urllib3

import Speak


class web_requests:

    def __init__(self, link, message):

        try:
            http = urllib3.PoolManager()

            r = http.request('GET', link)

            r.status

            Speak.Speak(message)

        except:

            Speak.Speak('problem with request')

            pass
