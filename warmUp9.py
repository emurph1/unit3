#Emily Murphy
#2017-10-04
#warmUp9.py - asks for word, print out with the vowels capitalized

word = input('Enter word: ')
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch =='u': #can also say ch in 'aeiouAEIOU'
        print(ch.upper())
    else:
        print(ch)
