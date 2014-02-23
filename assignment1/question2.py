import json
import Image

class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file
    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    def __init__(self, headline, content, creator, related_image = None):
        self.headline = headline
        self.content = content
        self.creator = creator
        self.related_image = related_image

    @staticmethod
    def fromFile(filename):
        rep = open(filename, 'r')
        rep = json.load(rep)
        return Article(rep["headline"], 
                       rep["content"],
                       rep["creator"],
                       Picture(rep["related_image"]["path"],
                               rep["related_image"]["creator"]))
        
    def show(self):
        print self.headline + "\n"
        print "By: " + self.creator + "\n"
        print self.content + "\n"

    def save(self, filename):
        f = open(filename, 'w')
        text = json.dumps({"headline" : self.headline, 
                           "creator" : self.creator,
                           "content" : self.content,
                           "related_image" : {
                               "path" : self.related_image.path,
                               "creator" : self.related_image.creator
                           }})
        f.write(text)
        
        

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    def __init__(self, path, creator):
        self.path = path
        self.creator = creator
    def show(self):
        Image.open(self.path).show()
