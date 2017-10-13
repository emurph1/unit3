#Emily Murphy
#2017-10-13
#quiz3.py -

for i in range(-5,6):
    print(i)

i = 18    
while i <= 32:
    print(i)
    i += 1
    
total = 0
for i  in range(13, 332):
    if i%2 != 0:
        total += i
print(total)

while True:
    word = input('Enter a word:')
    for ch in word:
        if ch == 'z':
            break