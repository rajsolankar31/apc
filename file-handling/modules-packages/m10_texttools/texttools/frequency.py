def word_frequency(tokens):
    f = {}
    for t in tokens: f[t] = f.get(t, 0) + 1
    return f
