#Emily Murphy
#2017-09-29
#divisors.py -

num = int(input('Enter a number: '))
i = 1
while i <= num :
    if num%i == 0:
        print(i)
    i += 1
    