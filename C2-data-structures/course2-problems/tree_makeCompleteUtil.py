"""make the given binary tree perfect
None -> -1"""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def getHeight(root):
    if root == None:
        return 0
    return (1+max(getHeight(root.left), getHeight(root.right)))

def makePerfect(root):
    dq = collections.deque([(root, 1)])
    result = []
    max_lvl = getHeight(root)
    cur_lvl = 1
    result.append(root.key)
    while(len(dq)):
        tu = dq.popleft()
        node = tu[0]
        lvl = tu[1]
        if lvl == max_lvl:
            break
        if node == -1:
            dq.append((-1, lvl+1))
            dq.append((-1, lvl+1))
            result.append(-1)
            result.append(-1)
        else:
            
            if node.left != None:
                dq.append((node.left, lvl+1))
                result.append(node.left.key)
            else:
                dq.append((-1, lvl+1))
                result.append(-1)
                
            if node.right != None:
                dq.append((node.right, lvl+1))
                result.append(node.right.key)
            else:
                dq.append((-1, lvl+1))
                result.append(-1)
    return result

if __name__ == '__main__':
    tree = Node(3)
    tree.right = Node(5)
    tree.left = Node(2)
    #tree.right.left = Node(6)
    #tree.right.right = Node(7)
    tree.left.left = Node(1)
    tree.left.right = Node(4)
    #tree.left.left.right = Node(8)
    #tree.left.left.right.left = Node(9)
    print(makePerfect(tree))
