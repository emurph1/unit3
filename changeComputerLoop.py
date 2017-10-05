#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
quarter = 25
dime = 10
nickel = 5
penny = 1
i = 1
while i <= 4:
    if cents-(25*i)== 0:
        print('Quarters:', i)
while i <= 10:
    if cents -(10*i) == 0:
        print('Dimes:', i)