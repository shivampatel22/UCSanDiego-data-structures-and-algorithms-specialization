class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def InorderTraversal(root):
    s = []
    current = root
    if root is None:
        return
    while(True):
        if current is not None:
            s.append(current)
            current = current.left
        elif(s):
            current = s.pop()
            print(current.data, end = ' ')
            current = current.right
        else:
            break
if __name__ == '__main__':       
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
  
    InorderTraversal(root) 
        
            