"""tree traversals (store the tree as array)"""
import sys, threading, collections

sys.setrecursionlimit(10**6) 
threading.stack_size(2**27)  

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
      
  def inOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        traverse(self.left[node])
        self.result.append(self.key[node])
        traverse(self.right[node])
    traverse(0)
    return self.result
    
  def preOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        self.result.append(self.key[node])
        traverse(self.left[node])
        traverse(self.right[node])
    traverse(0)
    return self.result
    
  def postOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        traverse(self.left[node])
        traverse(self.right[node])
        self.result.append(self.key[node])
    traverse(0)
    return self.result

  def levelOrder(self):
      self.result = []
      node = 0
      dq = collections.deque([node])
      while (len(dq) != 0):
          N = dq.popleft()
          self.result.append(self.key[N])
          if self.left[N] != -1:
            dq.append(self.left[N])
          if self.right[N] != -1:
            dq.append(self.right[N])
      return self.result    
    
def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))
	print(" ".join(str(x) for x in tree.levelOrder()))
threading.Thread(target = main).start()
