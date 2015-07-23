# Natural Language Toolkit: code_findtags

 def findtags(tag_prefix, tagged_text):
     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
     return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

 >>> tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
 >>> for tag in sorted(tagdict):
 ...     print(tag, tagdict[tag])
 ...
 NN [('year', 137), ('time', 97), ('state', 88), ('week', 85), ('man', 72)]
 NN$ [("year's", 13), ("world's", 8), ("state's", 7), ("nation's", 6), ("company's", 6)]
 NN$-HL [("Golf's", 1), ("Navy's", 1)]
 NN$-TL [("President's", 11), ("Army's", 3), ("Gallery's", 3), ("University's", 3), ("League's", 3)]
 NN-HL [('sp.', 2), ('problem', 2), ('Question', 2), ('business', 2), ('Salary', 2)]
 NN-NC [('eva', 1), ('aya', 1), ('ova', 1)]
 NN-TL [('President', 88), ('House', 68), ('State', 59), ('University', 42), ('City', 41)]
 NN-TL-HL [('Fort', 2), ('Dr.', 1), ('Oak', 1), ('Street', 1), ('Basin', 1)]
 NNS [('years', 101), ('members', 69), ('people', 52), ('sales', 51), ('men', 46)]
 NNS$ [("children's", 7), ("women's", 5), ("janitors'", 3), ("men's", 3), ("taxpayers'", 2)]
 NNS$-HL [("Dealers'", 1), ("Idols'", 1)]
 NNS$-TL [("Women's", 4), ("States'", 3), ("Giants'", 2), ("Bros.'", 1), ("Writers'", 1)]
 NNS-HL [('comments', 1), ('Offenses', 1), ('Sacrifices', 1), ('funds', 1), ('Results', 1)]
 NNS-TL [('States', 38), ('Nations', 11), ('Masters', 10), ('Rules', 9), ('Communists', 9)]
 NNS-TL-HL [('Nations', 1)]

