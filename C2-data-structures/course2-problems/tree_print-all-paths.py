"""print all the paths in a tree (path -> root to leaf)."""
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def printPaths(root):
    """modified iterative dfs"""
    stack = []
    key_stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            key_stack.append(current.key)
            current = current.left
        elif(stack):
            current = stack[-1]
            if (current.left is None)and(current.right is None):
                print(key_stack)
                curr_pop = stack.pop()
                key_stack.pop()
                while (len(stack) != 0)and(curr_pop == stack[-1].right):
                    curr_pop = stack.pop()
                    key_stack.pop()
            current = stack[-1].right
        else:
            break
    return

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
    printPaths(tree)
                
            
