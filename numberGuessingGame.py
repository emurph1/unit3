#Emily Murphy
#2017-09-29
#numberGuessingGame.py -


for i in range(1, 101):
    guess = int(input('Enter a guess: '))
    if guess < 63:
        print('Too low')
    elif guess > 63:
        print('Too high')
    elif guess == 63:
        print('You got it in', i, 'tries')
        break
