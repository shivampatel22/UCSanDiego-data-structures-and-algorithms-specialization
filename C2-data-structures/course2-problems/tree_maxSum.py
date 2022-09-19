"""Given a binary tree with a value associated with each node, we need to choose a subset of these nodes such that sum of chosen nodes is maximum
under a constraint that no two chosen node in subset should be directly connected that is, if we have taken a node in our sum then we can’t take
its any children in consideration and vice versa."""
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

def maxSum(root):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s1 = sum(grandChild(root))
    if root is not None:
        s2 = sum(grandChild(root.left)) + sum(grandChild(root.right))
        s4 = sum(grandChild(root.right))
        if root.left is not None:
            s3 = sum(grandChild(root.left))
            s4 += sum(grandChild(root.left.left)) + sum(grandChild(root.left.right))
        if root.right is not None:
            s3 += sum(grandChild(root.right.left))+sum(grandChild(root.right.right))
    print(s1,s2,s3,s4)
    return max(s1,s2,s3,s4)
    

def grandChild(node):
    arr = []
    def traverse(node):
        if node is None:
            return
        arr.append(node.data)
        if node.left is not None:
            traverse(node.left.left)
            traverse(node.left.right)
        if node.right is not None:
            traverse(node.right.left)
            traverse(node.right.right)
    traverse(node)
    return arr
    
    

if __name__ == '__main__':
    tree = Node(6)
    #tree.left = Node(3)
    tree.right = Node(8)
    #tree.left.left = Node(1)
    #tree.left.right = Node(5)
    tree.right.left = Node(10)
    tree.right.right = Node(11)
    
    print(maxSum(tree))
    
   
