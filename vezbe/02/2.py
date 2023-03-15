class Robot:
    """Predstavlja robota sa imenom """
    
    # klasan pristup
    population = 0  
    
    def __init__(self, name):
        self.name = name
        Robot.population += 1
    
    # deinicijalizacija    
    def __del__(self):
        Robot.population -= 1
    
        
    def say_hi(self):
        print(f'New message from {self.name}')
    
    @classmethod
    def how_many(cls):
        print(f'We have {cls.population} robots.')
        
    # @staticmethod # za staticke metode u klasi
    

if __name__ == '__main__':
    r1 = Robot('R24')
    r2 = Robot('R12-D4')
    r3 = Robot('T15')
    
    r1.say_hi()
    r2.say_hi()
    
    r1.how_many()
    
    del r1
    
    r2.how_many()