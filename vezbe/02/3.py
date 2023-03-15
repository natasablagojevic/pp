# Demostracija nasledjivanja

class Shape:
    
    # da bi promenljive bile private potrebno je da pocinju sa __
    # _ za nasledjivanje
    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled 
        
    def get_color(self):
        return self.__color
    
    def get_filled(self):
        return self.__filled 
    
    def set_filled(self, value):
        self.__filled = value 
        
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(color='red', filled=True)
        self.__length = length 
        self.__width = width 
        
    def get_area(self):
        return self.__length * self.__width 
    
    def get_perimeter(self):
        return 2*self.__length + 2*self.__width 
    
    def str(self):
        print(f'a: {self.__length}, b: {self.__width}, color: {self.get_color()}, filled: {self.get_filled}')

if __name__ == '__main__':
    s1 = Shape('red', True)
    
    # print(dir(s1))
    
    # print(s1._Shape__color)
    # print(s1.get_color())
    # print(s1.get_filled())
    
    r1 = Rectangle(5, 10)
    
    print(r1.get_area())
    
    r1.str()
    
    