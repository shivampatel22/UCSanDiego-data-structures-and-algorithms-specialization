"""find if two nodes in the given tree are cousins
cousins -> Two nodes are cousins if:
1: they are not siblings (children of same parent).
2: they are on the same level."""
import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

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

def getLevel(root, node, cur_lvl):
    if node == None:
        return -1
    if root == None:
        return 0 
    if root == node:
        return cur_lvl
    lvl = getLevel(root.left, node, cur_lvl+1)
    if lvl != 0:
        return lvl
    lvl = getLevel(root.right, node, cur_lvl+1)
    return lvl

def areCousins(root, node1, node2):
    if getParent(root, node1) == getParent(root, node2):
        return "No"
    elif getLevel(root, node1, 1) == getLevel(root, node2, 1):
        return "Yes"
    else:
        return "No"

def main():
    tree = Node(1)
    tree.right = Node(3)
    tree.left = Node(2)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.left.right = Node(8)
    tree.left.left.right.left = Node(9)
    #print(getLevel(tree, tree.right.right, 1))
    print(areCousins(tree, tree.left, tree.right))
    print(areCousins(tree, tree.left.left, tree.right.right))
    
threading.Thread(target = main).start()        
