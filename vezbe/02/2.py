class Robot:
    """Predstavlja robota sa imenom """
    
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print(f'New message from {self.name}')
        

if __name__ == '__main__':
    r1 = Robot('R24')
    r2 = Robot('R12-D4')
    r3 = Robot('T15')
    
    r1.say_hi()
    r2.say_hi()
    
    