def MyGener():

    for i in range(2):
        yield i

    yield 'aufshg'
    yield 123
    yield (12, 3)

if __name__ == '__main__':

    m = MyGener()

    print(m.__next__())
    print(m.__next__())
    print(m.__next__())
    print(m.__next__())
    print(m.__next__())
    print(m.__next__())
    print(m.__next__())
    
