#Emily Murphy
#2017-10-12
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))

q = 0
d = 0
n = 0
p = 0

while cents >= 25:
    cents = cents - 25
    q += 1
while cents >= 10:
    cents = cents - 10
    d += 1
while cents >= 5:
    cents = cents - 5
    n +=1
while cents >= 1:
    cents = cents - 1
    p +=1
    
print('Quarters:', q)
print('Dimes:', d)
print('Nickels:', n)
print('Pennies:', p)

