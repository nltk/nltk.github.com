# Natural Language Toolkit: code_modal_tabulate

 def tabulate(cfdist, words, categories):
     print('{:16}'.format('Category'), end=' ')                    # column headings
     for word in words:
         print('{:>6}'.format(word), end=' ')
     print()
     for category in categories:
         print('{:16}'.format(category), end=' ')                  # row heading
         for word in words:                                        # for each word
             print('{:6}'.format(cfdist[category][word]), end=' ') # print table cell
         print()                                                   # end the row

 >>> from nltk.corpus import brown
 >>> cfd = nltk.ConditionalFreqDist(
 ...           (genre, word)
 ...           for genre in brown.categories()
 ...           for word in brown.words(categories=genre))
 >>> genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
 >>> modals = ['can', 'could', 'may', 'might', 'must', 'will']
 >>> tabulate(cfd, modals, genres)
 Category            can  could    may  might   must   will
 news                 93     86     66     38     50    389
 religion             82     59     78     12     54     71
 hobbies             268     58    131     22     83    264
 science_fiction      16     49      4     12      8     16
 romance              74    193     11     51     45     43
 humor                16     30      8      8      9     13

