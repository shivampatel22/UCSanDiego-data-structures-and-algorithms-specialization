"""Find depth of deepest odd level leaf node"""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def levelOrder(root):
    dq = collections.deque([(root, 1)])
    result = []
    while (len(dq)!=0):
        tu = dq.popleft()
        node = tu[0]
        lvl = tu[1]
        if lvl%2 != 0:
            result.append((node, lvl))
        if node.left is not None:
            dq.append((node.left, lvl+1))
        if node.right is not None:
            dq.append((node.right, lvl+1))
    return result

def findDepth(tree):
    res = levelOrder(tree)
    #print(res)
    l = len(res)
    for i in range(l-1, -1, -1):
        if res[i][0].left is None and res[i][0].right is None:
            return (res[i][1])
                


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
    print(findDepth(tree))
                
            
