class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def InorderTraversal(root):
    if root is None:
        return
    InorderTraversal(root.left)
    print(root.data, end = ' ')
    InorderTraversal(root.right)
    
    
def PreorderTraversal(root):
    if root is None:
        return
    print(root.data, end = ' ')
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)
    
def PostorderTraversal(root):
    if root is None:
        return
    PostorderTraversal(root.left)
    PostorderTraversal(root.right)  
    print(root.data, end = ' ')
    
    
if __name__ == '__main__':
    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')
    root.left.left = Node('A')
    root.left.right = Node('D')
    root.left.right.left = Node('C')
    root.left.right.right = Node('E')
    root.right.right = Node('I')
    root.right.right.left = Node('H')
    print("inorder:")
    InorderTraversal(root)
    print("\npreorder:")
    PreorderTraversal(root)
    print("\npostorder:")
    PostorderTraversal(root)