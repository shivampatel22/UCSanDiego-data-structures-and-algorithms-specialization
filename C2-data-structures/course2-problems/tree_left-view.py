"""print left view of the given tree"""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def leftView(root):
    dq = collections.deque([(root, 0)])
    curr_lvl = 0
    result = []
    result.append(root.key)
    while (len(dq) != 0):
        tu = dq.popleft()
        node = tu[0]
        lvl = tu[1]
        if lvl > curr_lvl:
            result.append(node.key)
            curr_lvl = lvl
        if node.left is not None:
            dq.append((node.left, lvl+1))
        if node.right is not None:
            dq.append((node.right, lvl+1))
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
    print(leftView(tree))
                
            
