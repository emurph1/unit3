#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
print(today)
fri = weekday(date.today().year,date.today().month, 13)
fridate = date.today().year,date.today().month, 13
i = 0
while i <= 7:
    i +=1
    print(fridate)

    
        
        

