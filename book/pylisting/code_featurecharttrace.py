# Natural Language Toolkit: code_featurecharttrace

 >>> tokens = 'Kim likes children'.split()
 >>> from nltk import load_parser # [_load_parser1]
 >>> cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)  # [_load_parser2]
 >>> for tree in cp.parse(tokens):
 ...     print(tree)
 ...
 |.Kim .like.chil.|
 Leaf Init Rule:
 |[----]    .    .| [0:1] 'Kim'
 |.    [----]    .| [1:2] 'likes'
 |.    .    [----]| [2:3] 'children'
 Feature Bottom Up Predict Combine Rule:
 |[----]    .    .| [0:1] PropN[NUM='sg'] -> 'Kim' *
 Feature Bottom Up Predict Combine Rule:
 |[----]    .    .| [0:1] NP[NUM='sg'] -> PropN[NUM='sg'] *
 Feature Bottom Up Predict Combine Rule:
 |[---->    .    .| [0:1] S[] -> NP[NUM=?n] * VP[NUM=?n] {?n: 'sg'}
 Feature Bottom Up Predict Combine Rule:
 |.    [----]    .| [1:2] TV[NUM='sg', TENSE='pres'] -> 'likes' *
 Feature Bottom Up Predict Combine Rule:
 |.    [---->    .| [1:2] VP[NUM=?n, TENSE=?t] -> TV[NUM=?n, TENSE=?t] * NP[] {?n: 'sg', ?t: 'pres'}
 Feature Bottom Up Predict Combine Rule:
 |.    .    [----]| [2:3] N[NUM='pl'] -> 'children' *
 Feature Bottom Up Predict Combine Rule:
 |.    .    [----]| [2:3] NP[NUM='pl'] -> N[NUM='pl'] *
 Feature Bottom Up Predict Combine Rule:
 |.    .    [---->| [2:3] S[] -> NP[NUM=?n] * VP[NUM=?n] {?n: 'pl'}
 Feature Single Edge Fundamental Rule:
 |.    [---------]| [1:3] VP[NUM='sg', TENSE='pres'] -> TV[NUM='sg', TENSE='pres'] NP[] *
 Feature Single Edge Fundamental Rule:
 |[==============]| [0:3] S[] -> NP[NUM='sg'] VP[NUM='sg'] *
 (S[]
   (NP[NUM='sg'] (PropN[NUM='sg'] Kim))
   (VP[NUM='sg', TENSE='pres']
     (TV[NUM='sg', TENSE='pres'] likes)
     (NP[NUM='pl'] (N[NUM='pl'] children))))

