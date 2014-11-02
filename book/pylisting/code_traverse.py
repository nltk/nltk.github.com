# Natural Language Toolkit: code_traverse

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=" ")
    else:
        # Now we know that t.node is defined
        print('(', t.label(), end=" ")
        for child in t:
            traverse(child)
        print(')', end=" ")

 >>> t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
 >>> traverse(t)
 ( S ( NP Alice ) ( VP chased ( NP the rabbit ) ) )

