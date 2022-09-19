"""find the level of the given node"""
import sys
class Node():
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def findLevel(self, root, node, cur_lvl):
        if node > self.n:
            return 
        if root == -1:
            return 0 
        if root == node:
            return cur_lvl
        lvl = self.findLevel(self.left[root], node, cur_lvl+1)
        if lvl != 0:
            return lvl
        lvl = self.findLevel(self.right[root], node, cur_lvl+1)
        return lvl

if __name__ == '__main__':
    tree = Node()
    tree.read()
    print(tree.findLevel(0, 5, 1))
            
