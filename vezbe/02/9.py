# Fibonaci
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def Fibonaci():
    p = 0
    pp = 1
    sledeci = 0

    while True:
        yield p 
        p, pp = pp, p + pp 

if __name__ == '__main__':
    f = Fibonaci()
    
    for _ in range(10):
        print(f.__next__())
