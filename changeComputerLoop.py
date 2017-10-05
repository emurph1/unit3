#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1
while i <= 4:
    quarters = cents - (25*i)
    print(quarters)
    i += 1