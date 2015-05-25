# Natural Language Toolkit: code_dictionary

 >>> from collections import defaultdict
 >>> counts = defaultdict(int)
 >>> from nltk.corpus import brown
 >>> for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
 ...     counts[tag] += 1
 ...
 >>> counts['NOUN']
 30640
 >>> sorted(counts)
 ['ADJ', 'PRT', 'ADV', 'X', 'CONJ', 'PRON', 'VERB', '.', 'NUM', 'NOUN', 'ADP', 'DET']

 >>> from operator import itemgetter
 >>> sorted(counts.items(), key=itemgetter(1), reverse=True)
 [('NOUN', 30640), ('VERB', 14399), ('ADP', 12355), ('.', 11928), ...]
 >>> [t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]
 ['NOUN', 'VERB', 'ADP', '.', 'DET', 'ADJ', 'ADV', 'CONJ', 'PRON', 'PRT', 'NUM', 'X']

