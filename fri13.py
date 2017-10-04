#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
day = weekday(date.today().year,date.today().month,date.today().day)
month = date.today().month
year = date.today().year

i=0
while i< 10:
    day = weekday(year,month,13)
    if day == 4:
        print(month,'13',year)
        i+=1
    month = month + 1 
    if month > 12:
        month = 1
        year += 1 
        
        


