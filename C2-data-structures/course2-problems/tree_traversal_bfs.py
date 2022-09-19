"""beadth first traversal using queueu."""
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.Q = [None] * capacity
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self):
        return self.size == self.capacity
        
    def Enqueue(self, data):
        if self.isFull():
            print("queue full.")
            return
        self.rear = (self.rear + 1)%self.capacity
        self.Q[self.rear] = data
        self.size = self.size + 1
        return
        
    def Dequeue(self):
        if self.isEmpty():
            print("queue empty.")
            return
        curr = self.Q[self.front]
        self.front = (self.front + 1)%self.capacity
        self.size = self.size - 1
        return curr
    
def LevelTraversal(root):
    if root is None:
        return
    q = Queue(5)
    q.Enqueue(root)
    while not q.isEmpty():
        node = q.Dequeue()
        print(node.data, end = ' ')
        if node.left is not None:
            q.Enqueue(node.left)
        if node.right is not None:
            q.Enqueue(node.right)
    
    
if __name__ == '__main__':
    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')
    root.left.left = Node('A')
    root.left.right = Node('D')
    root.left.right.left = Node('C')
    root.left.right.right = Node('E')
    root.right.right = Node('I')
    root.right.right.left = Node('H')
    LevelTraversal(root)