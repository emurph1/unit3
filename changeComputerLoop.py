#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
quarters = (cents//25)
dimes = ((cents - (25 * quarters))//10)
nickels = ((cents - ((10 * dimes) + (25 * quarters)))//5)
pennies = ((cents - ((5 * nickels) + (10 * dimes) + (25 * quarters)))//1)
i = 0
while i <= cents:
    i += 1
print(quarters)
print(dimes)
print(nickels)
print(pennies)
