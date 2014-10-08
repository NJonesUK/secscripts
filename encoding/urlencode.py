import urllib2
import sys

while True:
	char=sys.stdin.read(1)
	print urllib2.quote(char[0].encode("utf8"))
