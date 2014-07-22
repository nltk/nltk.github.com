# Natural Language Toolkit: code_modal_tabulate

 def tabulate(cfdist, words, categories):
     print '%-16s' % 'Category',
     for word in words:                                  # column headings
         print '%6s' % word,
     print
     for category in categories:
         print '%-16s' % category,                       # row heading
         for word in words:                              # for each word
             print '%6d' % cfdist[category][word],       # print table cell
         print                                           # end the row

