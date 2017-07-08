
from gutenberg.cleanup import strip_headers
from gutenberg.acquire import load_etext
import string


def get_clean_text(fileid):
    try:
        raw = load_etext(fileid)
        text = strip_headers(raw).strip()
        raw_title = text.split('\n', 1)[0]
        tidy_title = raw_title.translate(str.maketrans('', '', string.punctuation))
        return({"title": tidy_title, "text": text})
    except Exception as e:
        print(e)
        pass
        return({})


if __name__ == '__main__':
    doc = get_clean_text(102)
    print(doc['title'])
    print(doc['text'][0:500])
