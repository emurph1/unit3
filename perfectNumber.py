#Emily Murphy
#2017-09-30
#perfectNumber.py - tells whether number is perfect or not

num = int(input('Enter a number: '))
i = 1
while i <= num:
    i += 1
    if num%i == 0:
        total = i + i
        if total == num:
            print('Perfect')
else:
    print('Not Perfect')
