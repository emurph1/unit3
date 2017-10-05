#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1
j = 1
c = 1
d = 1
while i <= 4:
    i += 1
    j += 1
    c += 1
    d += 1
    quarter = cents-(25*i)
    if quarter >= 0:
      dime = quarter - (10*j)
      if dime >= 0:
          nickel = dime - (5*c)
          if nickel >= 0:
              penny = nickel -(1*d)
             
print('Quarters:', i)                  
print('Nickels:',j)           
print('Dimes:', c)
print('Pennies:', d)
              