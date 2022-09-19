"""BST implementation -> balance -> AVL property"""
import random
def computeHeight(root):
    if root is None:
        return 0
    return max(computeHeight(root.left), computeHeight(root.right)) + 1
    
def height(node):
    if node is None:
        return -1
    else:
        return node.height

def updateHeight(node):
    node.height = max(height(node.left), height(node.right)) + 1


class BSTnode(object):
    def __init__(self, key):
        self.key = key
        self.disconnect()
    def disconnect(self):
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

class BST_AVL(object):
    def __init__(self):
        self.root = None

        
    def leftRotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x.parent.left is x:
                y.parent.left = y
            elif x.parent.right is x:
                y.parent.right = y
        x.parent = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        updateHeight(x)
        updateHeight(y)


    def rightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x.parent.left is x:
                y.parent.left = y
            elif x.parent.right is x:
                y.parent.right = y
        x.parent = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        updateHeight(x)
        updateHeight(y)


    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else: u.parent.right = v
        if v != None:
            v.parent = u.parent
            

    def next(self, node):
        #case 1: find the left descendant
        if node.right is not None:
            node = node.right
            while(node.left is not None):
                node = node.left
            return node
        
        #case 2: find the right ancestor
        else:
            n = node
            while (node.parent != None) and (node.parent.key < node.key):
                node = node.parent
            if node.parent is not None:
                return node.parent
            else:
                return n
            
        
    def insert(self, key):
        newNode = BSTnode(key)
        if self.root is None:
            self.root = newNode
        else:
            node = self.root
            while(True):
                if key < node.key:
                    #go left
                    if node.left is None:
                        node.left = newNode
                        newNode.parent = node
                        break
                    node = node.left
                else:
                    #go right
                    if node.right is None:
                         node.right = newNode
                         newNode.parent = node
                         break
                    node = node.right
        return


    def delete(self, node):
        p = node.parent
        #case 1: one or no child
        #case 1a: no left child or no child
        if node.left == None:
            self.transplant(node, node.right)
        #case 1b: no right child
        elif node.right == None:
            self.transplant(node, node.left)
        #case 2: both child are not none
        else:
            #find successor
            N = self.next(node)
            #if successor is not the right child of node to be deleted
            if N.parent != node:
                p = N.parent
                #promote right child of successor
                self.transplant(N, N.right)
                N.right = node.right
                N.right.parent = N
            self.transplant(node, N)
            N.left = node.left
            N.left.parent = N
        return p


    def find(self, key):
        node = self.root
        while(node is not None):
            if node.key == key:
                return node
            elif key < node.key:
                if node.left is not None:
                    node = node.left
                else: return node
            elif key > node.key:
                if node.right is not None:
                    node = node.right
                else: return node
        return None

    
    def AVLinsert(self, key):
        self.insert(key)
        N = self.find(key)
        self.rebalance(N)

    def AVLdelete(self, node):
       M = self.delete(node)
       self.rebalance(M)

    def rebalance(self, node):
        while(node is not None):
            updateHeight(node)
            
            if height(node.left) >= height(node.right)+2:
                if height(node.left.left) >= height(node.left.right):
                    self.rightRotate(node)
                else:
                    self.leftRotate(node.left)
                    self.rightRotate(node)
                    
            elif height(node.right) >= height(node.left)+2:
                if height(node.right.right) >= height(node.right.left):
                    self.leftRotate(node)
                else:
                    self.rightRotate(node.right)
                    self.leftRotate(node)
                    
            node = node.parent

    def printBST(self):
        node = self.root
        print("inorder traversal:")
        def traverse(n):
            if n == None:
                return
            traverse(n.left)
            print(n.key)
            traverse(n.right)
        traverse(node)

if __name__ == '__main__':
    tree1 = BST_AVL()
    tree2 = BST_AVL()
    items = []
    i = 0
    while i < 10:
        num = random.randint(1,20)
        if num not in items:
            items.append(num)
            i += 1
    print(items)
    for item in items:
        tree1.AVLinsert(item)
        tree2.insert(item)
    tree1.printBST()
    print("height after avl-insert -> {}".format(height(tree1.root)))
    print("height without avl-insert -> {}".format(computeHeight(tree2.root)-1))
    print("delete: {}".format(tree1.root.left.key))
    tree1.AVLdelete(tree1.root.left)
    print("height after avl-delete -> {}".format(height(tree1.root)))
    tree1.printBST()
    
    
                
