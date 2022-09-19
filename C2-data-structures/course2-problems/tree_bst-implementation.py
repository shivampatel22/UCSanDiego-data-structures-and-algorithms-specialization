"""BST implementation (without AVL)
1. insert
2. find
3. next
4. range search
5. delete
6. find and delete minimum"""
import random
class BSTnode(object):
    def __init__(self, key):
        self.key = key
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None

class BST(object):
    def __init__ (self):
        self.root = None

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

    def rangeSearch(self, x, y):
        res = []
        node = self.find(x)
        while(node.key <= y):
            if node.key >= x:
                res.append(node)
            node = self.next(node)
            if node.key == y:
                res.append(node)
                break
        return res

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else: u.parent.right = v
        if v != None:
            v.parent = u.parent
        

    def delete(self, node):
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
                #promote right child of successor
                self.transplant(N, N.right)
                N.right = node.right
                N.right.parent = N
            self.transplant(node, N)
            N.left = node.left
            N.left.parent = N

    def deleteMin(self):
        node = self.root
        if node.left is not None:
            while (node.left is not None):
                node = node.left
        self.delete(node)
        return node

    def printBST(self, node):
        print("inorder traversal:")
        def traverse(n):
            if n == None:
                return
            traverse(n.left)
            print(n.key)
            traverse(n.right)
        traverse(node)
            
if __name__ == '__main__':
    #create BST
    tree = BST()
    items = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for item in items:
        tree.insert(item)
    tree.printBST(tree.root)
    #find and next
    print("\n****find and next****\n")
    s = random.sample(items, 5)
    print("keys to be found ->{}".format(s))
    for elem in s:
        Node = tree.find(elem)
        print("key -> {} found".format(Node.key))
        print("next greater for {} -> {}".format(elem,(tree.next(Node)).key))
    #range search
    print("\n****range search****\n")
    test_set = []
    for i in range(10):
        s1 = random.sample(items, 2)
        if s1[0] < s1[1]:
            test_set.append(s1)
    print("sets: {}".format(test_set))
    i = 1
    for rng in test_set:
        print("set"+str(i)+": {}".format(rng))
        r = tree.rangeSearch(rng[0], rng[1])
        for elem in r:
            print(elem.key)
        i+=1
    #find and delete minimum
    print("\n****find and delete****\n")
    print("deleted {} from BST".format((tree.deleteMin()).key))
    print("deleted {} from BST".format((tree.deleteMin()).key))
    
        
    
       
    
    
        
        
        
