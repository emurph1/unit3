#Emily Murphy
#2017-09-30
#perfectNumber.py - tells whether number is perfect or not

num = int(input('Enter a number: '))
i = 0
while i <= num:
    i += 1
    if num%i == 0:
        print(i)
        total = i*i
        if total == num:
            print(total)
            print('Perfect')
            break
else:
    print('Not perfect')

        


