from PyDictionary import PyDictionary

import Keyword_Extract

import Speak


def Dictionary(word):

    word_extracted = Keyword_Extract.extract_keywords_from_text(word)

    dictionary = PyDictionary(word_extracted[-1])

    meaning = dictionary.getMeanings()

    synonyms = dictionary.getSynonyms()

    Speak.Speak(meaning)

    Speak.Speak(synonyms)

    print(dictionary.printMeanings())

    print(dictionary.getSynonyms())


