"""stack implementation using linked list.Push -> pushFront(), pop -> popFront()."""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def printList(self):
        "prints the list."
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def pushFront(self, data):
        """pushes a new node at the start of the list.Create a new node with data and point pointer of new node to
        head and then update head to point at this new node."""
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def popFront(self):
        "pops out the first node.Point head to the second node."
        self.head = self.head.next
        
    def isEmpty(self):
        """returns a bool depending on whether or not list is empty."""
        if self.head is None:
            return True
        else:
            return False
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.pushFront(0)
    llist.printList()
    