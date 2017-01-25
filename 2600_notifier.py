#!/usr/bin/python
import re
import feedparser
url = 'http://www.2600.com/rss.xml'
f = "/home/mike/code/2600_notifier/log.txt"
d = feedparser.parse(url)
fh = open(f, 'r+')
line = fh.readline()
line = line.strip()
if line != d['entries'][0]['link']:
    if re.match(r'(WINTER|SPRING|SUMMER|AUTUMN)\s+ISSUE\s+OF\s+2600\s+RELEASED', d['entries'][0]['title']):
        print d['entries'][0]['title'] + " " + d['entries'][0]['link'] + "\n"
fh.seek(0)
fh.truncate()
fh.write(d['entries'][0]['link'])
fh.close()
