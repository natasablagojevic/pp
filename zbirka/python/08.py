import math
import random

def faktorijel(n):
    p = 1
    for i in range(1, n+1):
        p *= i
        
    return p 

if __name__ == '__main__':
    print(faktorijel(6))
    print(int(math.log(125, 5)))
    print(random.random())