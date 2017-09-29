#Emily Murphy
#2017-09-29
#numberGuessingGame.py -

from random import randint
num = randint(1,100)
for i in range(1, 101):
    guess = int(input('Enter a guess: '))
    if guess < num:
        print('Too low')
    elif guess > num:
        print('Too high')
    elif guess == num:
        print('You got it in', i, 'tries')
        break
