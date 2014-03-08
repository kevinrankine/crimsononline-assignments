from question1 import (Content, Article, Picture)
import datetime as d

print
print "Creating a Content object..."
raw_input("Press enter to continue.")

today = d.datetime.strptime("2014/02/27", "%Y/%m/%d")
C1 = Content("gus-mayopoulos-comedian-UC", "this is an article", "BAILEY M. TRELA", today)
C1.show()

print
print "Creating same content, but as article..."
raw_input("Press enter to continue.")

A1 = Article("gus-mayopoulos-comedian-UC", "this is an article", "BAILEY M. TRELA", today)
A1.show()

print
print "Creating and opening image..."
raw_input("Press enter to continue.")

otherday = d.datetime.strptime("2014/03/02", "%Y/%m/%d")
P1 = Picture("mens-basketball-vs-columbia-2014-rivard", "this is a picture", "robert", otherday, "beauty.jpg")
P1.show()

print
print "A1 should match url"
raw_input("Press enter to continue.")

if A1.matches_url("http://www.thecrimson.com/article/2014/2/27/gus-mayopoulos-comedian-UC/"):
    print "It matched :-)"
else:
    print "It didn't match :-("

print
print "A1 shouldn't match url"
raw_input("Press enter to continue.")

if A1.matches_url("http://www.thecrimson.com/article/2014/3/2/harvard-tops-columbia-secures-share-of-title/"):
    print "It matched :-("
else:
    print "It didn't match :-}"

print

print "P1 should match url"
raw_input("Press enter to continue.")
print
if P1.matches_url("http://www.thecrimson.com/image/2014/3/2/mens-basketball-vs-columbia-2014-rivard/"):
    print "It matched :-)"
else:
    print "It didn't match :-("

print "Testing from_url, should display beauty..."
print

Content.from_url([C1, A1, P1], "http://www.thecrimson.com/image/2014/3/2/mens-basketball-vs-columbia-2014-rivard/").show()

print "Testing posted_after, should display image again..."
raw_input("Press enter to continue.")
other = d.datetime.strptime("2014/03/1", "%Y/%m/%d")

Content.posted_after([C1, A1, P1], other)[0].show()
