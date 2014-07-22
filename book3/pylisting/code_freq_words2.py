# Natural Language Toolkit: code_freq_words2

def freq_words(url):
    text = nltk.clean_url(url)
    freqdist = nltk.FreqDist(word.lower() for word in word_tokenize(text))
    return freqdist

