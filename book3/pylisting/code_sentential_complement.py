# Natural Language Toolkit: code_sentential_complement

def filter(tree):
    child_nodes = [child.node for child in tree
                   if isinstance(child, nltk.Tree)]
    return  (tree.node == 'VP') and ('S' in child_nodes)

