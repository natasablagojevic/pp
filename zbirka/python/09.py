def f(x, y, z):
    pass 

def kvadrat(x):
    return x**2

def translacija(x):
    return x-1

kvadrat1 = lambda x: x**2 


if __name__ == '__main__':
    print("kvadrat: ", kvadrat(5))
    print("kvadrat1: ", kvadrat1(5))
    print("translacija: ", translacija(4))    