"""Given A binary Tree, how do you remove all the half nodes (which has only one child)?
Note: leaves should not be touched as they have both children as NULL."""
import collections
class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = data

def delHalf(root):
    dq = collections.deque([(root, None)])
    while(len(dq)):
        tu = dq.popleft()
        node = tu[0]
        parent = tu[1]
        if node.left is not None and node.right is not None:
            dq.append((node.left, node))        
            dq.append((node.right, node))
        elif node.left is not None or node.right is not None:
            if parent == None:
                if node.left is not None:
                    root = node.left
                    dq.append((root, None))
                if node.right is not None:
                    root = node.right
                    dq.append((root,None))
            if parent.left == node:
                if node.left is not None:
                    parent.left = node.left
                    dq.append((node.left,parent))
                else:
                    parent.left = node.right
                    dq.append((node.right,parent))
            elif parent.right == node:
                if node.left is not None:
                    parent.right = node.left
                    dq.append((node.left,parent))
                else:
                    parent.right = node.right
                    dq.append((node.right,parent))
    return root

                    
