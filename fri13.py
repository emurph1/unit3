#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
print(today)
print(weekday(2013,2,14))

