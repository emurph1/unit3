#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
i = 1
while i <= 4:
    i += 1
    totalq = cents -(25*i)
    if totalq >= 0:
        print(totalq)
        totald = totalq -(10*i)
        if totald >= 0:
            print(totald)
            totaln = totald - (5*i)
            if totaln >= 0:
                print(totaln)
                totalp = totaln - (1*i)
                if totalp >= 0:
                    print(totalp)
print('Quarters:', i)
print('Dimes:', i)
print('Nickels:', i)
print('Pennies:', i)
    
    
