"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""
import re

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    f = open(filename)
    text = f.read().lower()
    words = re.findall(re.compile('\w+'), text)
    occurrences = {}
    
    for w in words:
        if w in occurrences:
            occurrences[w] += 1
        else:
            occurrences[w] = 1
    return sorted(occurrences, key = occurrences.get, reverse = True)
def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(filename)
    text = f.read().lower()
    words = re.findall(re.compile('\w+'), text)
    words = filter(lambda w : len(w) >= min_chars, words)
    occurrences = {}
        
    for w in words:
        if w in occurrences:
            occurrences[w] += 1
        else:
            occurrences[w] = 1

    return sorted(occurrences, key = occurrences.get, reverse = True)
    
def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    f = open(filename)
    text = f.read().lower()
    words = re.findall(re.compile('\w+'), text)
    words = filter(lambda w : len(w) >= min_chars, words)
    occurrences = {}
        
    for w in words:
        if w in occurrences:
            occurrences[w] += 1
        else:
            occurrences[w] = 1

    result = sorted(occurrences, key = occurrences.get, reverse = True)
    return [(w, occurrences[w]) for w in result]

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        return common_words_tuple(filename, min_chars)
    except(IOError):
        print "Something went wrong with reading the file :-("
