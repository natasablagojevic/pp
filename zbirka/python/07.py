import sys 
import random 
import os 

def faktorijel(n):
    p = 1
    for i in range(1, n+1):
        p *= i 
    
    return p

if __name__ == '__main__':
    print(sys.argv)
    
    print(faktorijel(5))
    print(math.factorial(5))
    print(math.log(5))