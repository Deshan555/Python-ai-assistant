
import pandas as pd

import random

import Speak


def suggest_movies():

    data = pd.read_csv("movies.csv")

    choice: list = random.choice(data[['Title', 'Rating', 'Rank']].values)

    return choice


def talk():

    data = suggest_movies()

    Speak.Speak("I can suggest you "+data[0])

    Speak.Speak("that movie hold "+str(data[2])+"th place on IMDB Top 250 Ranking List")

    Speak.Speak(data[0]+"achieves"+str(data[1])+" ratings out of ten")

    print("I can suggest you "+data[0])

    print("that movie hold "+str(data[2])+"th place on IMDB Top 250 Ranking List")

    print(data[0]+"achieves"+str(data[1])+" ratings out of ten")


