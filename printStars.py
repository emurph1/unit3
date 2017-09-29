#Emily Murphy
#2017-09-28
#printStars.py -

rows = int(input('Enter number of rows you want: '))
for i in range(rows):
    print(' '*(rows-i-1) + '*'*(2*i+1))
    
