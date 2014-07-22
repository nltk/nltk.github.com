# Natural Language Toolkit: code_convert_parens

def convert_parens(tokens):
    stack = [[]]
    for token in tokens:
        if token == '(':     # push
            sublist = []
            stack[-1].append(sublist)
            stack.append(sublist)
        elif token == ')':   # pop
            stack.pop()
        else:                # update top of stack
            stack[-1].append(token)
    return stack[0]

