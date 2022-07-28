import requests

import bs4

import Speak

import random

respond: list = ["According my knowledge", "Google said", "Best answer for your question is"]


def google_answers(question: str):

    query = question.lower()

    url = "https://www.google.com/search?q=" + query.replace(" ", "+")

    request_result = requests.get(url)

    soup = bs4.BeautifulSoup(request_result.text, "html.parser")

    # The answer is stored inside the class "BNeawe".

    temp = soup.find("div", class_='BNeawe').text

    Speak.Speak(random.choice(respond)+temp)

    print(temp)




