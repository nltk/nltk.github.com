# Natural Language Toolkit: code_brill_demo

 >>> from nltk.tbl import demo as brill_demo
 >>> brill_demo.demo()
 Training Brill tagger on 80 sentences...
 Finding initial useful rules...
     Found 6555 useful rules.

            B      |
    S   F   r   O  |        Score = Fixed - Broken
    c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
    o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
    r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
    e   d   n   r  |  e
 ------------------+-------------------------------------------------------
   12  13   1   4  | NN -> VB if the tag of the preceding word is 'TO'
    8   9   1  23  | NN -> VBD if the tag of the following word is 'DT'
    8   8   0   9  | NN -> VBD if the tag of the preceding word is 'NNS'
    6   9   3  16  | NN -> NNP if the tag of words i-2...i-1 is '-NONE-'
    5   8   3   6  | NN -> NNP if the tag of the following word is 'NNP'
    5   6   1   0  | NN -> NNP if the text of words i-2...i-1 is 'like'
    5   5   0   3  | NN -> VBN if the text of the following word is '*-1'
    ...
 >>> print(open("errors.out").read())
              left context |    word/test->gold     | right context
 --------------------------+------------------------+--------------------------
                           |      Then/NN->RB       | ,/, in/IN the/DT guests/N
 , in/IN the/DT guests/NNS |       '/VBD->POS       | honor/NN ,/, the/DT speed
 '/POS honor/NN ,/, the/DT |    speedway/JJ->NN     | hauled/VBD out/RP four/CD
 NN ,/, the/DT speedway/NN |     hauled/NN->VBD     | out/RP four/CD drivers/NN
 DT speedway/NN hauled/VBD |      out/NNP->RP       | four/CD drivers/NNS ,/, c
 dway/NN hauled/VBD out/RP |      four/NNP->CD      | drivers/NNS ,/, crews/NNS
 hauled/VBD out/RP four/CD |    drivers/NNP->NNS    | ,/, crews/NNS and/CC even
 P four/CD drivers/NNS ,/, |     crews/NN->NNS      | and/CC even/RB the/DT off
 NNS and/CC even/RB the/DT |    official/NNP->JJ    | Indianapolis/NNP 500/CD a
                           |     After/VBD->IN      | the/DT race/NN ,/, Fortun
 ter/IN the/DT race/NN ,/, |    Fortune/IN->NNP     | 500/CD executives/NNS dro
 s/NNS drooled/VBD like/IN |  schoolboys/NNP->NNS   | over/IN the/DT cars/NNS a
 olboys/NNS over/IN the/DT |      cars/NN->NNS      | and/CC drivers/NNS ./.

