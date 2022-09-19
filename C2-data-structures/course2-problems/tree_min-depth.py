"""print the minimum depth of the given tree.(min_depth -> the length of the shortest path from root to any leaf)"""
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def getMinDepth(TREE):
    if TREE is None:
        return 0
    return (1 + min(getMinDepth(TREE.left), getMinDepth(TREE.right)))



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
    print(getMinDepth(tree))
