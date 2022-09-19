"""calculating height of a binary tree. Height = maximum depth + 1."""
class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
def cal_Height(root):
    if root is None:
        return 0
    h = 1 + max(cal_Height(root.left), cal_Height(root.right)) 
    return h 

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("height of the tree is {}".format(cal_Height(root)))
        