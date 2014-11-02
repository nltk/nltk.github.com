# Natural Language Toolkit: code_wfst

 def init_wfst(tokens, grammar):
     numtokens = len(tokens)
     wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
     for i in range(numtokens):
         productions = grammar.productions(rhs=tokens[i])
         wfst[i][i+1] = productions[0].lhs()
     return wfst

 def complete_wfst(wfst, tokens, grammar, trace=False):
     index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
     numtokens = len(tokens)
     for span in range(2, numtokens+1):
         for start in range(numtokens+1-span):
             end = start + span
             for mid in range(start+1, end):
                 nt1, nt2 = wfst[start][mid], wfst[mid][end]
                 if nt1 and nt2 and (nt1,nt2) in index:
                     wfst[start][end] = index[(nt1,nt2)]
                     if trace:
                         print("[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                         (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end))
     return wfst

 def display(wfst, tokens):
     print('\nWFST ' + ' '.join(("%-4d" % i) for i in range(1, len(wfst))))
     for i in range(len(wfst)-1):
         print("%d   " % i, end=" ")
         for j in range(1, len(wfst)):
             print("%-4s" % (wfst[i][j] or '.'), end=" ")
         print()
 >>> tokens = "I shot an elephant in my pajamas".split()
 >>> wfst0 = init_wfst(tokens, groucho_grammar)
 >>> display(wfst0, tokens)
 WFST 1    2    3    4    5    6    7
 0    NP   .    .    .    .    .    .
 1    .    V    .    .    .    .    .
 2    .    .    Det  .    .    .    .
 3    .    .    .    N    .    .    .
 4    .    .    .    .    P    .    .
 5    .    .    .    .    .    Det  .
 6    .    .    .    .    .    .    N
 >>> wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
 >>> display(wfst1, tokens)
 WFST 1    2    3    4    5    6    7
 0    NP   .    .    S    .    .    S
 1    .    V    .    VP   .    .    VP
 2    .    .    Det  NP   .    .    .
 3    .    .    .    N    .    .    .
 4    .    .    .    .    P    .    PP
 5    .    .    .    .    .    Det  NP
 6    .    .    .    .    .    .    N

