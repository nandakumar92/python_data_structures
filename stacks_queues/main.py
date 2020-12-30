class stack:
    def __init__(self):
        self.stack=[]

    
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    def pop(self):
        return self.stack.pop()

    def push(self,val):
        self.stack.append(val)

    def count(self):
        return len(self.stack)

    def pop_element(self):
        return self.stack[-1]

class queue:
    def __init__(self):
        self.queue=[]
  
    def is_empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    
    def count(self):
        return len(self.queue)

    def dequeue(self):
        self.queue.pop(0)
    
    def enqueue(self,val):
        self.queue.append(val)

s=stack()
print(s.is_empty())
for i in range(10):
    s.push(i)
print(s.pop())
print(s.count())


    