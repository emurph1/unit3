#Emily Murphy
#2017-10-06
#baseConverter.py - input a number then convert it to any base from base 2 to 16
    
from math import log10
num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert to: '))
#use logs to find the largest power of the base that goes into the number
#there are other ways to do this if you have not yet learned about logs
power = log10(num)//log10(base)
answer = ''
while power >= 0:
digit = int(num/(base**power))
if digit<10:
answer += str(digit)
elif digit == 10:
answer += 'A'
elif digit == 11:
answer += 'B'
elif digit == 12:
answer += 'C'
elif digit == 13:
answer += 'D'
elif digit == 14:
answer += 'E'
else:
answer += 'F'
num -= digit*base**power
power -= 1
print('The answer is', answer)
    
