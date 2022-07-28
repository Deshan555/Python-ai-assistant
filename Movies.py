
import requests

import Config

import Speak

TMDB_API_KEY = Config.TMDB_API_KEY


def get_trending_movies():

    trending_movies = []

    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()

    results = res["results"]

    for r in results:

        trending_movies.append(r["original_title"])

    return trending_movies[:5]


def list_movies():

    movie_list = get_trending_movies()

    print(movie_list)

    Speak.Speak("According my opinions I suggest you to watch "+movie_list[0])

    Speak.Speak("or you can try to watch "+movie_list[1])

    Speak.Speak("But i think "+movie_list[2]+"may be a good idea to watch")

    Speak.Speak("Not only them, try movie "+movie_list[3]+"and"+movie_list[4]+"top movies in this week")


