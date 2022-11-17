# where does the sun rise first
from datetime import datetime
import pytz
list1 = ['Europe/Belfast', 'PRC', 'Australia/South']
dict1 = {}
str_date = '2019-12-15 12:00:00'
l_date_time = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
for j in list1:
    EST_TimeZone = pytz.timezone(j)
    data = EST_TimeZone.localize(l_date_time)
    #print(j,data)
    if (str(data).__contains__("+")):
        est = (str(data).split('+')[1])
        dict1[j] = 1*int(est.replace(':',''))
        #print(j, data,'+',est)
    else:
        est = (str(data).split(':')[2].split('-')[1])
        dict1[j] = -1 * int(est.replace(':', ''))
        #print(j, data,'-',est)
print(max(dict1, key = dict1.get))

