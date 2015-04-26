# Natural Language Toolkit: code_slashcfg

 >>> nltk.data.show_cfg('grammars/book_grammars/feat1.fcfg')
 % start S
 # ###################
 # Grammar Productions
 # ###################
 S[-INV] -> NP VP
 S[-INV]/?x -> NP VP/?x
 S[-INV] -> NP S/NP
 S[-INV] -> Adv[+NEG] S[+INV]
 S[+INV] -> V[+AUX] NP VP
 S[+INV]/?x -> V[+AUX] NP VP/?x
 SBar -> Comp S[-INV]
 SBar/?x -> Comp S[-INV]/?x
 VP -> V[SUBCAT=intrans, -AUX]
 VP -> V[SUBCAT=trans, -AUX] NP
 VP/?x -> V[SUBCAT=trans, -AUX] NP/?x
 VP -> V[SUBCAT=clause, -AUX] SBar
 VP/?x -> V[SUBCAT=clause, -AUX] SBar/?x
 VP -> V[+AUX] VP
 VP/?x -> V[+AUX] VP/?x
 # ###################
 # Lexical Productions
 # ###################
 V[SUBCAT=intrans, -AUX] -> 'walk' | 'sing'
 V[SUBCAT=trans, -AUX] -> 'see' | 'like'
 V[SUBCAT=clause, -AUX] -> 'say' | 'claim'
 V[+AUX] -> 'do' | 'can'
 NP[-WH] -> 'you' | 'cats'
 NP[+WH] -> 'who'
 Adv[+NEG] -> 'rarely' | 'never'
 NP/NP ->
 Comp -> 'that'

