#!/usr/bin/env python

def fizzbuzz():
    for i in range(1,101):
        if i % 15 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
def swapchars(s):
    chars = ""
    occurences = {}
    for i in s:
        if i in occurences and i.isalpha():
            occurences[i.lower()] += 1 
        elif i.isalpha():
            occurences[i.lower()] = 1
    o = sorted(occurences, key = occurences.get)
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

def sortcat(n, *s):
    lnth = {}
    for w in s:
        lnth[w] = len(w)
    s = sorted(lnth, key = lnth.get)
    s.reverse()
    return "".join(s[:n])

from random import random as r

def random_direction():
    v = r()
    if v <= 0.2:
        return "U"
    elif v <= 0.4:
        return "D"
    elif v <= 0.6:
        return "L"
    elif v <= 0.8:
        return "R"
    else:
        return "F"
    
def luigi(trials):
    experiment = []
    num_wins = 0.0
    for i in range(trials):
        for i in range(3):
            experiment.append(random_direction())
        if not "F" in experiment:
            num_wins += 1
        experiment = []
    return num_wins / trials

"""
The actual probability is (4/5)*(4/5)*(4/5) = 0.512
"""
import urllib
import json
from datetime import datetime as d

def shuttleboy():
    url = "http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass%20Ave%20Garden%20St&output=json"
    data = urllib.urlopen(url)
    data = json.load(data)
    data = data[:3]
    for i in data:
        print "A shuttle departs at " + i["departs"][11:]
        current = d.strptime(d.now().strftime("%H:%M:%S"), "%H:%M:%S")
        delta = d.strptime(i["departs"][11:], "%H:%M:%S") - current
        print "in " + str(delta.seconds / 60) + "minutes."
