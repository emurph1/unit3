#Emily Murphy
#2017-10-01
#changeComputerLoop.py - asks for number of cents and outputs amount of each coin needed

cents = int(input('Enter number of cents: '))
totalq = cents/25
totald = totalq/10
totaln = totald/5
totalp = totaln/1
i = 0
while i == 4:
    i += 1
    if totalq != 0:
        print(totald)
        if totald != 0:
            print(totaln)
            if totaln != 0:
                print(totalp)
    
    
    
