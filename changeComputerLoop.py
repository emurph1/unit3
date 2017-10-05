#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1

while i <= 4:
    i += 1
    quarter = cents-(25*i) and >= 0
    dime = quarter - (10*i) and >= 0
    nickel = dime - (5*i) and >= 0
    penny = nickel -(1*i) and >= 0
    print('Quarters:', i)
    print('Dimes:', i):
    print('Nickels:',i)  
    print('Pennies:', i)
              