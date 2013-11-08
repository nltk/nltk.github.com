# Natural Language Toolkit: code_freq_words1

from bs4 import BeautifulSoup
from urllib import request

def freq_words(url, freqdist, n):
    text = nltk.clean_url(url)
    for word in nltk.word_tokenize(text):
        freqdist.inc(word.lower())
    print(freqdist.keys()[:n])

