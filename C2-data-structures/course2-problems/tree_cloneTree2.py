"""clone tree with random pointers(recursive)"""
def cloneTree(root):
    di = {}
    cloneLeftAndRight(root, di)
    cloneRandom(root, di)
    return di[root]

def cloneLeftAndRight(root, di):
    if root is None:
        return
    di[root] = Node(root.data)
    di[root].left = cloneLeftAndRight(root.left, di)
    di[root].right = cloneLeftAndRight(root.right, di)
    return di[root]

def cloneRandom(root, di):
    if root is None:
        return
    if root.random is not None:
        di[root].random = di[root.random]
    cloneRandom(root.left, di)
    cloneRandom(root.right, di)
    

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
