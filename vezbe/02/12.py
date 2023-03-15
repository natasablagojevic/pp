import sys
import os

# argumenti komandne linije

print(sys.argv)

# ispis trenutnog direktorijuma
print(os.curdir)

# ispis roditeljskog direktorijuma
print(os.pardir)

# apsolutna putanja do fajla
print(os.path.abspath(os.curdir))
print(os.path.abspath(os.pardir))


# seprator operator
print(os.sep)

# listanje direktorijuma
print(os.listdir('.'))

data = os.listdir('.')
paths = []

for name in data:
    path = os.path.join(os.path.abspath(os.curdir), name)
    paths += [path]

for p in paths:
    print(p)


# os.walk() rekurzivno obilazi direktorijum
for curr, poddirs, podfiles in os.walk('/home/natasa/Desktop/Fakultet/5_sem/'):
    print(curr)
    print(poddirs)
    print(podfiles)

    input()

# da li je fajl
os.path.isfile('putanja')

#da li je direktorijum
os.path.isdir('putanja')
