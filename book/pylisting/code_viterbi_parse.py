# Natural Language Toolkit: code_viterbi_parse

grammar = nltk.parse_pcfg('''
  NP  -> NNS [0.5] | JJ NNS [0.3] | NP CC NP [0.2]
  NNS -> "cats" [0.1] | "dogs" [0.2] | "mice" [0.3] | NNS CC NNS [0.4]
  JJ  -> "big" [0.4] | "small" [0.6]
  CC  -> "and" [0.9] | "or" [0.1]
  ''')
viterbi_parser = nltk.ViterbiParser(grammar)

