# Natural Language Toolkit: code_unusual

 def unusual_words(text):
     text_vocab = set(w.lower() for w in text if w.isalpha())
     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
     unusual = text_vocab - english_vocab
     return sorted(unusual)

 >>> unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
 ['abbeyland', 'abhorred', 'abilities', 'abounded', 'abridgement', 'abused', 'abuses',
 'accents', 'accepting', 'accommodations', 'accompanied', 'accounted', 'accounts',
 'accustomary', 'aches', 'acknowledging', 'acknowledgment', 'acknowledgments', ...]
 >>> unusual_words(nltk.corpus.nps_chat.words())
 ['aaaaaaaaaaaaaaaaa', 'aaahhhh', 'abortions', 'abou', 'abourted', 'abs', 'ack',
 'acros', 'actualy', 'adams', 'adds', 'adduser', 'adjusts', 'adoted', 'adreniline',
 'ads', 'adults', 'afe', 'affairs', 'affari', 'affects', 'afk', 'agaibn', 'ages', ...]

