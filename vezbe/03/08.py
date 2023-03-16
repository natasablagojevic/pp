# funkcije viseg reda
# map, filter, reduce

l = list(range(20))

print(l)

# map(fja, kolekcija)
# kolekcija mora da bude iterabilna

def kvadriraj(x):
    return x*x

# def: lambda fje
# lambda argumenti : telo

l1 = list(map(lambda x : x*x, l))

print(l1)

l2 = [x**2 for x in l]
print(l2)

# filtriranje:
# filter(fja, kolekcija)

l3 = list(filter(lambda x: x%2 == 0, l1))
print(l3)

l4 = [x**2 for x in l if x % 2 == 0]
print(l4)

l5 = list(filter(lambda x : x % 2 == 0, map(lambda x : x**2, l)))
print(l5)

# zip - zipuje listu
#       spaja svaki element iz prve liste, sa svakim elementom iz druge liste
#       katuje se na min(len(l1), len(l2)
z = list(zip([1, 2, 3], ['Ana', 'Aca', 'Aleksa']))
print(z)

# reduce
# vrsi redukciju liste, tako da listu slika u element
from functools import reduce
from functools import partial
import math
l = [i for i in range(10)]
print(reduce(lambda x, y: x+y, l))

def stepen(x, n):
    return math.pow(x, n)

kvadriraj = partial(stepen, n=2)
print(kvadriraj(5))
