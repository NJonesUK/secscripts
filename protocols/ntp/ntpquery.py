import ntplib
from time import ctime
import sys

c = ntplib.NTPClient()
response = c.request(sys.argv[1])
print ctime(response.tx_time)
