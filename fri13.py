#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

year = date.today().year
month = date.today().month
day = date.today().day
fri = weekday(date.today().year,date.today().month, 13 + 1)

i = 1
while i <= 10 and month < 13:
    i+=1
    fridate = (year, month, day)
    if fri == 4:
        print(fridate)
        
        


