class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        
        while not s.is_empty():
            item = s.pop()
            print(item)
