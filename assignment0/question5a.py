import urllib
import json
from datetime import datetime as d

def shuttleboy():
    url = "http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass%20Ave%20Garde\
n%20St&output=json"
    data = urllib.urlopen(url)
    data = json.load(data)
    data = data[:3]
    for i in data:
        output = ""
        output += "A shuttle departs at " + i["departs"][11:]
        current = d.strptime(d.now().strftime("%H:%M:%S"), "%H:%M:%S")
        delta = d.strptime(i["departs"][11:], "%H:%M:%S") - current
        output += " in " + str(delta.seconds / 60) + " minutes."
        print output
if __name__ == '__main__':
    shuttleboy()
