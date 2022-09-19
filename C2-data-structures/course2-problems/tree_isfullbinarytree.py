"""check if a binary tree is full or not
Theoram -> Any full binary tree has 2L - 1 nodes, where L is the number of leaf nodes in the tree."""
import collections
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def levelOrder(root):
    dq = collections.deque([root])
    cnt_leaf = 0
    cnt_nodes = 0
    while (len(dq)!=0):
        node = dq.popleft()
        cnt_nodes += 1
        if node.left is not None:
            dq.append(node.left)
        if node.right is not None:
            dq.append(node.right)
        if node.left is None and node.right is None:
            cnt_leaf += 1
    return (cnt_leaf, cnt_nodes)
                


if __name__ == '__main__':
    tree = Node(1)
    tree.right = Node(3)
    tree.left = Node(2)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.left.right = Node(8)
    tree.left.left.right.left = Node(9)
    leaves, nodes = levelOrder(tree)
    print("Yes" if 2*leaves - 1 == nodes else "No")
