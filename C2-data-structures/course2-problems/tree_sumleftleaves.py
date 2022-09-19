"""print sum of all the left leaves of the given tree"""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def levelOrder(root):
    dq = collections.deque([root])
    result = []
    while (len(dq)!=0):
        node = dq.popleft()
        if node.left is not None:
            dq.append(node.left)
            if node.left.left is None and node.left.right is None:
                result.append(node.left.key)
        if node.right is not None:
            dq.append(node.right)
    return sum(result)


if __name__ == '__main__':
    tree = Node(1)
    tree.right = Node(3)
    tree.left = Node(2)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.left.right = Node(8)
    tree.left.left.right.left = Node(9)
    print(levelOrder(tree))
                
            
