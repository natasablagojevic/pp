class A:
    def __init__(self):
        super().__init__()
        print('__init__ A')
    
    
class B:
    def __init__(self):
        super().__init__()
        print(super())
        
        print('__init__ B')
        
class C:
    def __init__(self):
        super().__init__()
        print(super())
        print('__init__ C')    
    
class X(A, B, C):
    def __init__(self):
        super().__init__()
            
    
if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    x = X()
    