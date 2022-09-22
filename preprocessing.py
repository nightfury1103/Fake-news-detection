import re


# Lower text func
def lower_text(text):
    return ' '.join(text.lower() for _ in text.split())


# Remove stopword func
def get_stopwords_list(stop_file_path):
    """load stop words """
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = {m.strip() for m in stopwords}
        return list(frozenset(stop_set))


vietnamese = get_stopwords_list('vietnamese_stopwords.txt')

temp = vietnamese.copy()
temp.sort()
temp.reverse()


def remove_stopwords(text):
    text_list = text.split()
    text_len = len(text_list)
    for word in temp:
        word_list = word.split()
        word_len = len(word_list)
        for i in range(text_len + 1 - word_len):
            if text_list[i:i + word_len] == word_list:
                text_list[i:i + word_len] = [None] * word_len
    return ' '.join(t for t in text_list if t)


# Remove noise func
TAG_1 = re.compile(r'<[^>]+>')
TAG_2 = re.compile("[@#$]")


def remove_tags(text):
    text = TAG_1.sub('', text)
    return TAG_2.sub('', text)


def remove_noise(text):
    return ' '.join(word for word in text.split() if word.isalnum())


# Text_processing func
def text_preprocessing(text):
    # lowercase
    text = text.lower()

    # Remove stopwords
    text = remove_stopwords(text)

    # Remove noise
    text = remove_tags(text)

    # Remove punctuations
    re.sub(r'[^\w\s]', '', text)

    return text
