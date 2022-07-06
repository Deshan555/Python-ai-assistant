from rake_nltk import Rake


def extract_keywords_from_text(txt: str):

    rake_nltk_var = Rake()

    text = txt

    rake_nltk_var.extract_keywords_from_text(text)

    keyword_extracted: list = rake_nltk_var.get_ranked_phrases()

    return keyword_extracted
