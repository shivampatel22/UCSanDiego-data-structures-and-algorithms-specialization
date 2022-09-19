"""queue implementation using array."""
class Queue():
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.Q = [None] * capacity
        self.capacity = capacity
        
    def isFull(self):
        return self.size == self.capacity
            
    def isEmpty(self):
        return self.size == 0
            
    def enqueue(self, data):
        if self.isFull():
            print("queue full.")
            return
        self.rear = (self.rear+1) % self.capacity
        self.Q[self.rear] = data
        self.size = self.size + 1
        print("enqueued " + str(data) + " to queue.")
        return
        
    def dequeue(self):
        if self.isEmpty():
            print("queue empty.")
            return
        print("dequeued " + str(self.Q[self.front]) + " from queue.")
        self.front = (self.front+1) % self.capacity
        self.size = self.size - 1
        return
            
    def topFront(self):
        if self.isEmpty():
            print("queue empty.")
            return
        print("front:" + str(self.Q[self.front]))
        return
            
    def topRear(self):
        if self.isEmpty():
            print("queue empty.")
            return
        print("rear:" + str(self.Q[self.rear]))
        return
        
    def printQueue(self):
        j = self.front
        print("current queue: ")
        for i in range(1, self.size + 1):
            print(self.Q[j], end = ' ')
            j = (j+1) % self.capacity
        return        
                
        
if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    #q.printQueue()
    q.dequeue()
    q.printQueue()
    
            
            
            
        