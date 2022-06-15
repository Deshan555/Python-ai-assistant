from pygooglenews import GoogleNews

import Pushbullet

import Speak

import os


class send_news:

    def __init__(self):

        index: int = 1

        news_list: list = []

        google_news = GoogleNews()

        get_news = google_news.search('Sri Lanka')

        file = open("temp.txt", "a")

        for entry in get_news["entries"]:

            if index <= 50:
                file.write(str(index) + " " + entry["title"])

                file.write("\n\n")
            else:
                break

            index = index + 1

        file.close()

        file = open("temp.txt", "r")

        Pushbullet.Push_bullet('News Requests', file.read())

        Speak.Speak('News Send To Your Device')

        file.close()

        os.remove("temp.txt")






