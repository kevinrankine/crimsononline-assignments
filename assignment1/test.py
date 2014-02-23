#!/usr/bin/env python

from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)

raw_input("Press enter to start.")
print "==testing question 1=="
print "common_words... ",
raw_input("Press enter to continue.")
pprint(common_words("words.txt"))

raw_input("Press enter to continue.")
print "common_words_min 2... ",
raw_input("Press enter to continue.")
pprint(common_words_min("words.txt", 2))

raw_input("Press enter to continue.")
print "common_words_min 5... ",
raw_input("Press enter to continue."),
pprint(common_words_min("words.txt", 5))

raw_input("Press enter to continue.")
print "common_words_min 9... ",
raw_input("Press enter to continue."),
pprint(common_words_min("words.txt", 9))

raw_input("Press enter to continue.")
print "common_words_tuple w/ min 5... ",
raw_input("Press enter to continue."),
pprint(common_words_tuple("words.txt", 5))

raw_input("Press enter to continue.")
print "common_words_safe... ",
raw_input("Press enter to continue."),
pprint(common_words_safe("words_fail.txt", 5))
print

from question2 import (Article, Picture)
import random

print "Testing question 2"
raw_input("Press enter to continue.")
print "Creating a ugly article..."
badArticle = Article("Aliens!", "There are aliens", "Not YB")

raw_input("Press enter to continue.")
print "Showing it..."
print "\n"
badArticle.show()

raw_input("Press enter to continue.")
print "loading a better article from article.json"
betterArticle = Article.fromFile("article.json")

raw_input("Press enter to continue.")
print "Showing the better article"
print "\n"
betterArticle.show()

raw_input("Press enter to continue.")
print "Changing the creator to random.random()"
betterArticle.creator = "{}".format(random.random())

raw_input("Press enter to continue.")
print "Showing the better article again, with new creator"
print("\n")
betterArticle.show()

raw_input("Press enter to continue.")
print "Saving the better article"
betterArticle.save("article.json")

raw_input("Press enter to continue.")
print "Creating a Picture"
prettyImage = Picture("beauty.jpg", "ya boy")

raw_input("Press enter to continue.")
print "Displaying Picture"
prettyImage.show()
