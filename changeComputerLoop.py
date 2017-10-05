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
    if cents - quarter == dime:
        print('Quarters:', i)
    elif cents - dime == nickel:
        print('Dimes:', i)
    elif cents - nickel == penny:
        print('Nickels:',i)
    elif cents - penny == 0:
        print('Pennies:', i)
    i += 1