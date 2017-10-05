#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1
while i <= 4:
    quarter = cents-(25*i)
    if quarter >= 0:
      dime = quarter - (10*i)
      if dime >= 0:
          nickel = dime - (5*i)
          if nickel >= 0:
              penny = nickel -(1*i)
             
print('Quarters:', i)                  
print('Nickels:',i)           
print('Dimes:', i)
print('Pennies:', i)
              
i += 1