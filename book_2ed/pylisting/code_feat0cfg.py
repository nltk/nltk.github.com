# Natural Language Toolkit: code_feat0cfg

 >>> nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
 % start S
 # ###################
 # Grammar Productions
 # ###################
 # S expansion productions
 S -> NP[NUM=?n] VP[NUM=?n]
 # NP expansion productions
 NP[NUM=?n] -> N[NUM=?n]
 NP[NUM=?n] -> PropN[NUM=?n]
 NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
 NP[NUM=pl] -> N[NUM=pl]
 # VP expansion productions
 VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
 VP[TENSE=?t, NUM=?n] -> TV[TENSE=?t, NUM=?n] NP
 # ###################
 # Lexical Productions
 # ###################
 Det[NUM=sg] -> 'this' | 'every'
 Det[NUM=pl] -> 'these' | 'all'
 Det -> 'the' | 'some' | 'several'
 PropN[NUM=sg]-> 'Kim' | 'Jody'
 N[NUM=sg] -> 'dog' | 'girl' | 'car' | 'child'
 N[NUM=pl] -> 'dogs' | 'girls' | 'cars' | 'children'
 IV[TENSE=pres,  NUM=sg] -> 'disappears' | 'walks'
 TV[TENSE=pres, NUM=sg] -> 'sees' | 'likes'
 IV[TENSE=pres,  NUM=pl] -> 'disappear' | 'walk'
 TV[TENSE=pres, NUM=pl] -> 'see' | 'like'
 IV[TENSE=past] -> 'disappeared' | 'walked'
 TV[TENSE=past] -> 'saw' | 'liked'

