def word_frequency(words):
    d={}
    for w in words: d[w]=d.get(w,0)+1
    return d
