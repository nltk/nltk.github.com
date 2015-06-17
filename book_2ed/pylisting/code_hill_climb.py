# Natural Language Toolkit: code_hill_climb

def flip(segs, pos):
    return segs[:pos] + `1-int(segs[pos])` + segs[pos+1:]
def hill_climb(text, segs, iterations):
    for i in range(iterations):
        pos, best = 0, evaluate(text, segs)
        for i in range(len(segs)):
            score = evaluate(text, flip(segs, i))
            if score < best:
                pos, best = i, score
        if pos != 0:
            segs = flip(segs, pos)
            print evaluate(text, segs), segment(text, segs)
    return segs

