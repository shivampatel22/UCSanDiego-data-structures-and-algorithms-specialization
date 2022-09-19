import sys
import threading

sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)  

class height(object):
    def __init__(self):
        self._node = 0
        self._child_node = []
        self._parent_node =[]
        self._root_node = 0
        
    def read(self):
        self._node = int(sys.stdin.readline())
        for _ in range(0, self._node):
            self._child_node.append([])
        self._parent_node = [int(num) for num in sys.stdin.readline().split()]
       
        for index,parent_node in enumerate(self._parent_node):
            if(parent_node == -1):
                self._root_node = index
            else:
                self._child_node[parent_node].append(index)
        
    def compute(self,root_node):
        maxHeight = 0
        for index in range(0,len(self._child_node[root_node])):
            maxHeight = max(maxHeight,self.compute(self._child_node[root_node][index]))
        return maxHeight + 1

    def compute_height(self):
        
        return self.compute(self._root_node)
            

def main():
    tree = height()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()