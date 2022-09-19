class stack():
    def __init__(self,size):
        self.maxsize = size
        self.arr = [None]*(size)
        self.size = 0 
        self.top = None
        
    def isFull(self):
        return self.size == self.maxsize
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self,ele):
        if self.isFull():
            print("stack is full")
            return
        if self.isEmpty():
            self.top = 0
        else:
            self.top = self.top+1
        self.arr[self.top] = ele
        self.size = self.size+1
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        self.top = self.top-1
        self.size = self.size-1
        
    def getTop(self):
        return self.arr[self.top]
    
    def printStack(self):
        for i in range(self.size-1, -1, -1):
            print(self.arr[i])
        
if __name__ == '__main__':
    si = int(input())
    a = [int(a) for a in input().split()]
    s1 = stack(si)
    for e in a:
        s1.push(e)
    s1.printStack()
    print("top -> {}".format(s1.getTop()))
    
            