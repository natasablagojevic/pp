"""
    immutable - nepromenljiv. postojan
"""

import sys 

if __name__ == '__main__':
    try:
        n = int(input("Unesite broj: "))
    except:
        sys.exit("Greska! Niste uneli ceo broj!")
        
    x = 'Hello'
    y = 'world'
    
    print(x, y)
    
    print(x + y)
    
    x = 'Hello world'
    y = 'Hello world'
    
    print(x == y)
    print (x + y)