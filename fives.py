#Emily Murphy
#2017-09-27
#fives.py - ask for a number then print out all the multiples of 5 to that number

num = int(input('Enter a number: '))

for i in range(1, num):
    i = i*5
    if i <= num:
        print(i)

