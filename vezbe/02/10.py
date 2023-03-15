import sys

# with open('./imena.txt', 'w') as f:
# 
    # f.write('Aca\n')
    # f.write('Ana\n')
    # f.write('Nikola\n')

try:
    with open('./imena1.txt', 'r') as f:
        # print(f.readlines())    # lista linija
        # print(f.read())         # ispisuje svaki red ponaosob sa svojim '\n'

        for line in f.read():
            for c in line:
                print(c)
except:
    sys.exit('Fajl ne postoji')
