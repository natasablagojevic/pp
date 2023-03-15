class Stek:
    # self se koristi da se oznaci da je to metoda klase
    # self je isto sto i this u Javi
    def __init__(self):
        self.items = []
        self.n = 0
        
    def push(self, element):
        self.items.append(element)
        self.n += 1

    def peek(self):
        try:
            return self.items[-1]
        except:
            print('Stek je prazan')
            return None
    
    def pop(self):
        try:
            self.n -= 1
            return self.items.pop()
        except:
            print('Nije moguce pop()')
            return None
    
    def size(self):
        return self.n

    
if __name__ == '__main__':
    s = Stek()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s.peek())

    