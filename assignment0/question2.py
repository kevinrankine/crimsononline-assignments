def swapchars(s):
    chars = ""
    occurences = {}
    for i in s:
        if i in occurences and i.isalpha():
            occurences[i.lower()] += 1
        elif i.isalpha():
            occurences[i.lower()] = 1
    o = sorted(occurences, key = occurences.get)
    if len(o) < 1:
        return s
    lowest = o[0]
    highest = o[len(o) - 1]
    for i in range(len(s)):
        if s[i] == lowest:
            chars += highest
        elif s[i].lower() == lowest:
            chars += highest.upper()
        elif s[i] == highest:
            chars += lowest
        elif s[i].lower() == highest:
            chars += highest.upper()
        else:
            chars += s[i]
    return chars
