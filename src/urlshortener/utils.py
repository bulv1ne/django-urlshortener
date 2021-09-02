import re

word_regex = re.compile(r"[a-z0-9]+")


def cleanup_wordlist(wordlist):
    for word in wordlist:
        word = cleanup_word(word)
        if word:
            yield word


def cleanup_word(word):
    match = word_regex.search(word.lower())
    if not match:
        return None
    return match.group(0)
