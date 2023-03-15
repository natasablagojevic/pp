class A:
    def explore(self):
        print('expore A')
        
class B(A):
    def explore(self):
        print('expore B')
        
if __name__ == '__main__':
    a = A()
    b = B()
    
    a.explore()
    b.explore()