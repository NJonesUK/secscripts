import sys

encodestring = sys.argv[1]
outstring = ''

for char in encodestring:
    outstring += str(ord(char))
    outstring += ','

print outstring