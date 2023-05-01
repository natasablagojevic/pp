import sys 
import random 
import os 
import math
import time

def faktorijel(n):
    p = 1
    for i in range(1, n+1):
        p *= i 
    
    return p

if __name__ == '__main__':
    print(sys.argv)
    
    try: 
        n = int(input("Unesite broj: "))
    except:
        sys.exit("Greska! Niste uneli broj!")
        
    print('faktorijel: ', math.factorial(n))
    print('log: ', math.log(n))
    print('exp: ', math.exp(n))
    
    print(random.random())
    
    os.system('ls -lt')
    
    print(time.time())