#!/usr/bin/python
import re
import feedparser
url = 'http://www.2600.com/rss.xml'
f = "/home/mike/code/2600_notifier/log.txt"
d = feedparser.parse(url)
fh = open(f, 'r+')
line = fh.readline()
if line != d['entries'][0]['link']:
	if re.match(r'(WINTER|SPRING|SUMMER|AUTUMN).*', d['entries'][0]['title']):
		print d['entries'][0]['title'] + " " + d['entries'][0]['link'] + "\r\n"
fh.seek(0)
fh.write(d['entries'][0]['link'] + "\r\n")
fh.truncate()
fh.close()
