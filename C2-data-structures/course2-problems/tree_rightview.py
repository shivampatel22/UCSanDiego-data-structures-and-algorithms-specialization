"""print right view of binary tree
"""
import collections

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def levelTraversal(root):
    result = []
    result.append(root.key)
    dq = collections.deque([(root,0)])
    curr_lvl = 0
    while(len(dq) != 0):
        #print(1)
        tu = dq.popleft()
        node = tu[0]
        if tu[1] > curr_lvl:
            result.append(node.key)
            curr_lvl = tu[1]
        if node.right is not None:
            dq.append((node.right, tu[1]+1))
            #print(node.right.key)
        if node.left is not None:
            dq.append((node.left, tu[1]+1))
            #print(node.left.key)
    return result

if __name__ == '__main__':
    tree = Node(1)
    tree.right = Node(3)
    tree.left = Node(2)
    tree.right.left = Node(6)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.left.right = Node(8)
    tree.right.left.right = Node(9)
    tree.left.left.right.right = Node(10)
    print("expected: [1, 3, 6, 9, 10] got:{}".format(levelTraversal(tree)))
    
    
        
        
        
