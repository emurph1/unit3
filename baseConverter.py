#Emily Murphy
#2017-10-02
#baseConverter.py - input a number then convert it to any base from base 2 to 16

num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert to? ')) 
if base == 2:
    i = 1
    while i <= num:
        i+=1
        print((num % 2))
        
    

