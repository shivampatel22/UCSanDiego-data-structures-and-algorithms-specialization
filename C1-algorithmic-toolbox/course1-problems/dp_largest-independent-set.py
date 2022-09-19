"""
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it.
A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset.
"""
class node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def solve(root):
    size = {}
    def traverse(root, size):
        if root is None:
            return
        traverse(root.left, size)
        size[root] = 0
        traverse(root.right, size)
    traverse(root, size)
    #print(size)
    ans = LIS(root, size)
    return ans
    
def LIS(root, size):
    if root is None:
        return 0
    
    if size[root] != 0:
        return size[root]
    
    if root.left == None and root.right == None:
        size[root] = 1
        return size[root]
    
    size_exc = LIS(root.left,size) + LIS(root.right,size)
    size_inc = 1
    if root.left is not None:
        size_inc += LIS(root.left.left,size) + LIS(root.left.right,size)
    if root.right is not None:
        size_inc += LIS(root.right.left,size) + LIS(root.right.right,size)
    size[root] = max(size_inc, size_exc)
    
    return size[root]

if __name__ == '__main__':
    root = node(20) 
    root.left = node(8) 
    root.left.left = node(4) 
    root.left.right = node(12) 
    root.left.right.left = node(10) 
    root.left.right.right = node(14) 
    root.right = node(22) 
    root.right.right = node(25)
    print("Size of the Largest Independent Set is ", solve(root)) 
