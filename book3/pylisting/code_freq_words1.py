# Natural Language Toolkit: code_freq_words1

from bs4 import BeautifulSoup
from urllib import request

def freq_words(url, freqdist, n):
    response = request.urlopen(url)
    html = response.read().decode('utf8')
    raw = BeautifulSoup(html).get_text()
    for word in word_tokenize(raw):
        freqdist[word.lower()] += 1
    print(freqdist.most_common(n))

