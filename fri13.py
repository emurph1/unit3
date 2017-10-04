#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().year, date.today().month, 13
year = date.today().year
month = date.today().month
fri = weekday(date.today().year,date.today().month, 13)
i = 1
while i <= 10:
    i+=1
    fridate = (year, month, 13)
    if fri == 4:
        month += 1
        print(fridate)
        


