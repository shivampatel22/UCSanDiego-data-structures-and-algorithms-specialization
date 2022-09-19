"""
Task: You are given a description of a rooted tree. Your task is to compute and output its height.
Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree,
not necessarily a binary tree.

Input Format: The first line contains the number of nodes n. The second line contains n integer numbers from −1 to n−1 — parents
of nodes. If the i-th one of them (0 ≤ i ≤ n−1) is −1, node i is the root, otherwise it’s 0-based index of the parent of i-th node. It is guaranteed that there
is exactly one root. It is guaranteed that the input represents a tree.
""" 
import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct(n, arr):
    nodes = [Node(i) for i in range(n)]
    for i in range(n):
        if arr[i] == -1:
            root = nodes[i]
        else:
            if nodes[arr[i]].left is None:
                nodes[arr[i]].left = nodes[i]
            else:
                nodes[arr[i]].right = nodes[i]
    return root

def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data)
    inOrder(node.right)

def getHeight(root):
    if root is None:
        return 0
    return (max(getHeight(root.left), getHeight(root.right))+1)

def main():
    n = int(sys.stdin.readline())
    arr = [int(x) for x in input().split()]
    print(getHeight(construct(n ,arr)))
threading.Thread(target = main).start()    
    
