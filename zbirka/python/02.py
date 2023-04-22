import sys

if __name__ == '__main__':
    try:
        a = int(input("Unesite prvi broj: "))
        b = int(input("Unesite drugi broj: "))
        niska = input("Unesite nisku: ")
    except:
        sys.exit("Greska! Los unos")
        
    print(a, b, niska)
    
    print('Zbir: ', a + b)
    print('Razlika: ', a - b)
    print('Proizvod: ', a*b)
    print('Kolicnik: ', a // b) # celobrojno deljenje
    print('Realno deljenje: ', a / b)