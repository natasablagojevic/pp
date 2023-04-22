import sys 

if __name__ == '__main__':
    try:
        niska = input("Unesite nisku: ")
        n = int(input("Unesite broj: "))
    except:
        sys.exit("Greska! Los ulaz!")
        
    print("Ispisivanje vise stringova: ")