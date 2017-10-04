#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().year, date.today().month, date.today().day 
year = date.today().year
month = date.today().month
day = 13
fri = weekday(date.today().year,date.today().month, date.today().day + 1)
i = 1
while i <= 10:
    i+=1
    fridate = (year, month, day)
    if fri == 4:
        print(fridate)


