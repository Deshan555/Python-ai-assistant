
import webbrowser

import Keyword_Extract


def img_find(txt: str):

    keyword_list: list = Keyword_Extract.extract_keywords_from_text(txt)

    base_url = "https://www.google.co.in/search?q="+keyword_list[-1]+"&source=lnms&tbm=isch"

    webbrowser.open(base_url, new=2)


