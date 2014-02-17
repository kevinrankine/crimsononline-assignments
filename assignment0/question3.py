def sortcat(n, *s):
    lnth = {}
    for w in s:
        if type(w) != str:
            w = str(w)
        lnth[w] = len(w)
    s = sorted(lnth, key = lnth.get)
    s.reverse()
    return "".join(s[:n])
