from textblob import TextBlob


def correct_sentence_spelling(sentence):

    sentence = TextBlob(sentence)

    result = sentence.correct()

    print(result)


