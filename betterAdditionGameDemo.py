#Emily Murphy
#2017-10-04
#betterAdditionGameDemo.py - asks addition problem until user gets 5 right

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is ' + str(num1) + ' + ' + str(num2) + '?'
    answer = int(input(question))
    if num1 + num2 == answer:
        print('Correct')
        numCorrect += 1
    else:
        print('The answer was', num1+num2)
        
print('Good job! You are not stupid!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

