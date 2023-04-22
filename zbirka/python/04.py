"""
    SUPPORTED COLORS:
    - blue.
    - green.
    - red.
    - cyan.
    - magenta.
    - yellow.
    - black.
    - white.
"""

import sys 
from termcolor import colored

if __name__ == '__main__':
    try:
        n = int(input("Unesite broj: "))
    except:
        sys.exit("Greska! Pogresan ulaz!")
    
    print(colored("Ostatak broja 5 je: ", 'blue'), colored(n % 5, 'green'))
    
    print("Prvih n brojeva:")
    for i in range(1, n+1):
        print(colored(i, 'green'))
        
    i = 1
    while (i <= n):
        print(i)
        i += 1