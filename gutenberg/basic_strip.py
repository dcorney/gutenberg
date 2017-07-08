from gutenberg.cleanup import strip_headers
import gutenberg.acquire.text as acquire
import string

# Minimal code to get a specified text from Project Gutenburg


def get_clean_text(fileid):
    try:
        raw = acquire.load_etext(fileid)
        tx = strip_headers.strip_headers(raw).strip()
        raw_title = tx.split('\n', 1)[0]
        tidy_title = raw_title.translate(str.maketrans('', '', string.punctuation))
        return({"title": tidy_title, "text": tx})
    except Exception as e:
        print(e)
        return({})


def dev():
    doc = get_clean_text(102)
    print(doc['title'])
    print(doc['text'][0:500])
