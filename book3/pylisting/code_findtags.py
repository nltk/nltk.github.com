# Natural Language Toolkit: code_findtags

 def findtags(tag_prefix, tagged_text):
     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
     return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

