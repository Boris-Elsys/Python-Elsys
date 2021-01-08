import math

num = int(input(""))

def nextPrime(num):
    
    next_num = num + 1
    prime = True
    
    while True:
        for i in range(2, next_num):
            if next_num % i == 0:
                prime = False
                break
            
        if prime == True:
            return next_num
            
        else:
            next_num = next_num + 1
            
            if next_num % 2 == 0:
                next_num = next_num + 1
            prime = True

print(nextPrime(num))

num2 = input()

def isDisarium(n):
    nsum = 0
    
    for i in range(len(n)):
        nsum = nsum + int(n[i]) ** (i + 1)
        
    if n == str(nsum):
        print(n + " is a disarium number.")
        
    else:
        print(n + " not a disarium number.")  
        
isDisarium(num2)