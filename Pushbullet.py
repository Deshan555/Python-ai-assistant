
from pushbullet import Pushbullet

API_KEY = "o.SwB5RE7PBYNdAOSSjOBE60FRalj4MECx"


class Push_bullet:

    def __init__(self, headline, message):

        bullet = Pushbullet(API_KEY)

        push = bullet.push_note(headline, message)