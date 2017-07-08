from cleanup import strip_headers
from acquire import load_etext
import string

# Minimal code to get a specified text from Project Gutenburg


def get_clean_text(fileid):
    try:
        raw = load_etext(fileid)
        text = strip_headers(raw).strip()
        raw_title = text.split('\n', 1)[0]
        tidy_title = raw_title.translate(str.maketrans('', '', string.punctuation))
        return({"title": tidy_title, "text": text})
    except Exception as e:
        print(e)
        return({})


def dev():
    doc = get_clean_text(102)
    print(doc['title'])
    print(doc['text'][0:500])
