# Natural Language Toolkit: code_traverse

def traverse(t):
    try:
        t.node
    except AttributeError:
        print(t, end=" ")
    else:
        # Now we know that t.node is defined
        print('(', t.node, end=" ")
        for child in t:
            traverse(child)
        print(')', end=" ")

