
from pushbullet import Pushbullet

import Config

API_KEY = Config.API_KEY


class Push_bullet:

    def __init__(self, headline, message):

        bullet = Pushbullet(API_KEY)

        push = bullet.push_note(headline, message)