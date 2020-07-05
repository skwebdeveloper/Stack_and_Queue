class Queue:
    def __init__(self):
        self.items = []
        
        
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)   
        
    def enque(self,item):
        return self.items.append(item)
    
    def deque(self):
        if self.is_empty():
            return
        return self.items.pop()
    
    def peek(self):
        return self.items[0]      
            
    
    def display(self):
        print(self.items)
                
        
if __name__ == "__main__":
    que = Queue()
    
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("0. EXit")      
        
        option = int(input("Enter your choice : ")) 
        
        if option == 1:
                x = int(input("Push your item : "))
                que.enque(x)
        elif option == 2:
                que.deque()
        elif option == 3:
            print(que.peek()) 
        elif option == 4:
            print(que.size())
        elif option == 5:
                que.display()
        elif option == 0:
            break
        else:
            print("Wrong Choice")
        print()          
                    