"""clone the given tree with random pointers(iteratve)"""
import collections
def cloneTree(root):
    di = {}
    dq = collections.deque([root])
    newNode = Node(root.data)
    di[root] = newNode
    newRoot = newNode
    dqClone = collections.deque([newRoot])
    while(len(dq)!=0 or len(dqClone)!=0):
        node = dq.popleft()
        nodeClone = dqClone.popleft()
        
        if node.left is not None:
            dq.append(node.left)
            newLeft = Node(node.left.data)
            di[node.left] = newLeft
            nodeClone.left = newLeft
            dqClone.append(newLeft)
        if node.right is not None:
            dq.append(node.right)
            newRight = Node(node.right.data)
            di[node.right] = newRight
            nodeClone.right = newRight
            dqClone.append(newRight)
    print(di)
    #print(root.left)
    #print(root.left.left.random)
    dq = collections.deque([root])
    while(len(dq)):
        node = dq.popleft()
        if node.random is not None:
            rand = di[node.random]
            di[node].random = rand
        if node.left is not None:
            dq.append(node.left)
            
        if node.right is not None:
            dq.append(node.right)
    return newRoot

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)
      

if __name__ == '__main__':
    tree = Node(6)
    tree.left = Node(3)
    tree.right = Node(8)
    tree.left.left = Node(1)
    tree.left.right = Node(5)
    tree.left.left.random = tree.left
    tree.left.right.random = tree
    printInorder(tree)
    clone = cloneTree(tree)
    printInorder(clone)
   




