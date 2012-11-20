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
                         print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                         (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
     return wfst

 def display(wfst, tokens):
     print '\nWFST ' + ' '.join([("%-4d" % i) for i in range(1, len(wfst))])
     for i in range(len(wfst)-1):
         print "%d   " % i,
         for j in range(1, len(wfst)):
             print "%-4s" % (wfst[i][j] or '.'),
         print

