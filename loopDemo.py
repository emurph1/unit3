#Emily Murphy
#2017-09-27
#loopDemo.py - demo on loops

"""
#print I love computer science 5 times
for i in range(0,5):
    print('I <3 Computer Science')"""

"""
# while loops
i = 1
while i <= 5:
    print('I <3 Computer Science')
    i = i+1 #new update for i because i is always less than 5, so code keeps running and the page will want kill
"""
"""
i = 1
while i<=20:
    print(i)
    i = i+1 """

"""i = 13
while i<=27:
    print(i)
    i = i+1"""


"""
#print the numbers from 1 to 20
for i in range(1,21):
    print(i) """
    
"""
#print out the odd nubers from 13 to 27 (%2 ==1 for odds and %2 == 0 for evens)
#third number tells how many to go up each time --> can do a negative number too
for i in range(13, 28, 2):
    print(i) """
   
""" 
#add up numbers from 1 to 5
total = 0
for i in range (1,6):
    total = total + i
print(total)"""

total = 0
i = 1
while i <=5:
    total= total + i # can also write total += i
    i = i+1 #can also i += 1
print(total)