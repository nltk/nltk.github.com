# Natural Language Toolkit: code_check_parens

def check_parens(tokens):
    stack = []
    for token in tokens:
        if token == '(':     # push
            stack.append(token)
        elif token == ')':   # pop
            stack.pop()
    return stack

