#Emily Murphy
#2017-10-02
#warmUp8.py - find sum of all integers less than 100,000 that are divisible by 3, 10, and 17

total = 0
for i in range(1,100000):
    if i % 3 == 0 and i % 10 == 0 and i % 17 == 0:
        total += i
print(total)
    
