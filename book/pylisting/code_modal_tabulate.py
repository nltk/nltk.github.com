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

