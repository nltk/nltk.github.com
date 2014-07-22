# Natural Language Toolkit: code_traverse

def traverse(t):
    try:
        t.node
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        print '(', t.node,
        for child in t:
            traverse(child)
        print ')',

