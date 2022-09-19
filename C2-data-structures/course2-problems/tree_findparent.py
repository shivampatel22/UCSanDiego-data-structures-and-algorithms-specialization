"""find the parent of the given node"""
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def getParent(root, node):
    if node == None:
        return -1
    if root == None:
        return
    if root.left == node or root.right == node:
        return root
    parent = getParent(root.left, node)
    if parent != None:
        return parent
    parent = getParent(root.right, node)
    return parent

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
    ans = getParent(tree, tree.right.right)
    print(ans.key if ans != -1 else -1)
