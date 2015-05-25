# Natural Language Toolkit: code_suffix_pos_tag

def pos_features(sentence, i): # [_suffix-pos-tag-fd]
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

