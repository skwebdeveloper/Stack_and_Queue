# ==================================================================        
# CIRCULAR QUEUE        
# ==================================================================        

class Circular:
    def __init__(self, default_size=10):
        self.front = 0
        self.count = 0
        self.items = [None] * default_size   
        
    def Enque(self, item):
        if self.count == len(self.items):
              self.resize(2*(len(self.item))
        i = (self.count + self.front) % len(self.items)
        self.items[i] = self.item
        count += 1
                           
    def Deque(self):
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        count -= 1
        return x

    def display(self):
        print(self.items)
        
                