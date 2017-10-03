#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().year, date.today().month, date.today().day 
year = date.today().year + 1
month = date.today().month + 1
day = 13
fri = weekday(date.today().year,date.today().month, day)
i = 1
while i <= 10:
    i+=1
    fridate = (year, month, day)
    if day == 13 and fri == 4:
        print(fridate)
        

