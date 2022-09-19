"""queue using two stacks"""
class queue():
    def __init__(self, maxsize):
        self.stack1 = []
        self.stack2 = []
        self.maxsize = maxsize
        
    def enqueue(self, el):
        if len(self.stack1) == self.maxsize:
            print("queue is full")
            return
        self.stack1.append(el)
        return

    def dequeue(self):
        if len(self.stack1) == 0:
            print("queue is empty")
            return
        
        if len(self.stack1) == 1:
            self.stack1.pop()
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        return

    def printQ(self):
        print(*self.stack1)

if __name__ == '__main__':
    size = int(input())
    arr = [int(x) for x in input().split()]
    q = queue(size)
    for elem in arr:
        q.enqueue(elem)
    q.printQ()
    q.dequeue()
    q.dequeue()
    print("after 2 dequeue")
    q.printQ()
