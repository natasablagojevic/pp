import sys
from termcolor import colored
# prvi dan u mesecu je ponedeljak
# napisati funkciju koja za prosledjeni argment koji je dan ispisuje dan u mesecu

dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak', 'subota', 'nedelja']

def radni_dan(n):
    print(dani[n%7-1])
    
    return True if n%7 -1 in range(0, 5) else False
    
    
if __name__ == '__main__':
    
    for _ in range(10):
        try:
            n = int(input("Unesite broj: "))
        except:
            sys.exit("Greska! Niste uneli broj!")
        
        print(radni_dan(n))
        