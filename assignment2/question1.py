import datetime
import re
import Image



class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self, title, subtitle, creator, pub_date):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.pub_date = pub_date

    def show(self):
        print "Title: {0}\nSubtitle: {1}\nCreator: {2}\nPublished on: {3}".format(self.title, self.subtitle, self.creator, self.pub_date.strftime("%Y/%m/%d"))

    def fix(self, c):
        if len(c) == 1:
            return '0' + c
        else:
            return c
            
    def matches_url(self, url):
        p = "http://www.thecrimson.com/(\w+)/(\\d+)/(\\d+)/(\\d+)/(.+)/"
        m = re.match(p, url)
        if not m:
            return 
        else:
            content_type = m.group(1)
            year = m.group(2)
            month = self.fix(m.group(3))
            day = self.fix(m.group(4))
            slug = m.group(5)
            if self.pub_date.strftime("%Y/%m/%d") == "{0}/{1}/{2}".format(year, month, day):
                if type(self) is Article and content_type == "article" and self.title == slug:
                    return True
                elif type(self) is Picture and content_type == "image" and self.title == slug:
                    return True
                else:
                    return False
            else:
                return False
    @classmethod
    def from_url(cls, l_con, url):
        l_con = filter(lambda c : c.matches_url(url), l_con)
        if len(l_con) == 0:
            return None
        elif len(l_con) == 1:
            return l_con[0]
        else:
            print "Duplicates in Content list"
            return None
    @classmethod
    def posted_after(cls, l_con, t):
        return filter(lambda c : c.pub_date - t > datetime.timedelta(0), l_con)
    
                    
            

class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, pub_date, related_image = None):
        super(Article, self).__init__(title, subtitle, creator, pub_date)
        self.related_image = related_image

    def show(self):
        super(Article, self).show()
        if self.related_image:
            Image.open(self.related_image.path)
    
        

class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, pub_date, image_file):
        super(Picture, self).__init__(title, subtitle, creator, pub_date)
        self.image_file = image_file
        
    def show(self):
        Image.open(self.image_file).show()
