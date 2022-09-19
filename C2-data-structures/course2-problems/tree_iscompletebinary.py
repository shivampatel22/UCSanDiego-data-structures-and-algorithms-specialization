"""print whether or not the given binary tree is complete.
complete tree -> a binary tree is said to be complete if all the levels of the tree are completely filled except possibly the last.
All the nodes on the last level are as left as possible."""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def isComplete(root):
    dq = collections.deque([root])
    flag = False
    while (len(dq)!=0):
        node = dq.popleft()
        if node.left is not None:
            if flag == True:
                return "No"
            dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)
            else:
                flag = True
        else:
            if node.right is not None:
                return "No"
            
    return "Yes"


if __name__ == '__main__':
    tree = Node(1)
    tree.right = Node(3)
    tree.left = Node(2)
    tree.right.left = Node(5)
    tree.right.right = Node(6)
    #tree.left.left = Node(4)
    tree.left.right = Node(4)
    #tree.left.left.right = Node(8)
    #tree.left.left.right.left = Node(9)
    print(isComplete(tree))

   
