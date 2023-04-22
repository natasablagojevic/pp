import random
import sys

def DNA(length):
    return ''.join(random.choice('CGTA' for _ in xrange(length)))

try:
    N = 10_000
    dna = DNA(N)
    with open('./bio_data.txt', 'w') as f:
        f.write(dna)
except:
    sys.exit("Greska")

# N = 10_000
# baza = 'CTGA'
# with open(file, 'w') as f:
#     for i in range(N):
#         for _ in range(random.randint(8, 12):
#             f.write()