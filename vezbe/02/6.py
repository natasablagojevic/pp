class Point: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
        
    # overloading operators
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    # overwritting
    def __add__(self, other):
        x = self.x + other.x 
        y = self.y + other.y 
        
        return Point(x, y)
    
    
if __name__ == '__main__':
    p1 = Point(1, 2)
    
    print(p1) 
    
    p2 = Point(10, -5)
    
    print(p1 + p2)