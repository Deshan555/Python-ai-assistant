from nltk import ne_chunk, pos_tag, word_tokenize

from nltk.tree import Tree


def name_recognizer(text: str):

    nltk_results = ne_chunk(pos_tag(word_tokenize(text)))

    name: str = ''

    for nltk_result in nltk_results:

        if type(nltk_result) == Tree:

            for nltk_result_leaf in nltk_result.leaves():

                name += nltk_result_leaf[0] + ' '

                print('Type: ', nltk_result.label(), 'Name: ', name)

                return name

    if len(name) == 0:

        print("none")

        return 'none'

