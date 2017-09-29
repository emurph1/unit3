#Emily Murphy
#2017-09-28
#guass.py 

total = 0
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter the difference number: '))
for i in range(num1, num2, num3):
    total += i
    print(total)
