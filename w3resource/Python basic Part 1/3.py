import time
from datetime import date

year = time.localtime().tm_year
month = time.localtime().tm_mon
day = time.localtime().tm_mday
hour = time.localtime().tm_hour
minutes = time.localtime().tm_min
seconds = time.localtime().tm_sec

print('%s-%s-%s %s:%s:%s' % (year,month,day,hour,minutes,seconds))

#Example

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

