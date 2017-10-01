#Emily Murphy
#2017-09-30
#perfectNumber.py - tells whether number is perfect or not

num = int(input('Enter a number: '))
i = 1
while 1 <= num:
    divisors = (num%1 == 0)
    total = divisors + divisors
    if total == num:
        print('Perfect')
    else:
        print('Not Perfect')
