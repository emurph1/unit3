#Emily Murphy
#2017-10-02
#fri13.py - prints out dates for the next 10 fridays the 13ths

from datetime import date
from calendar import weekday

today = date.today().day, date.today().month, date.today().year
friday = today + datetime.timedelta((4-today.weekday()) % 7 )
i = 1
for i in range(1,11):
    print(friday)
    
        
        

