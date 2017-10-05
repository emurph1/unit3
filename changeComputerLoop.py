#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1
quarter = cents-(25*i)
dime = cents-(10*i)
nickel = cents-(5*i)
penny = cents-(1*i)
while i <= 4:
    if quarter == 0:
        print('Quarters:', i)
    elif dime == 0:
        print('Dimes:', i)
    elif nickel == 0:
        print('Nickels:',i)
    elif penny == 0:
        print('Pennies:', i)
    i += 1