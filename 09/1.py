import random
import sys

def random_dna_sequence(length):
    return ''.join(random.choice('ACTG') for _ in range(length))

def base_frequency(ndna):
    d = {}
    for base in 'ATCG':
        d[base] = dna.count(base)/float(len(ndna))
    return d

for _ in range(20):
    dna = random_dna_sequence(100)
    print(dna, base_frequency(dna))

if __name__ == '__main__':
    try:
        with open("dna.txt", 'a') as f:
            for _ in range(50):
                dna = random_dna_sequence(100)
                dna += '\n'
                f.write(dna) 

    except:
        sys.exit('Greska!')   

