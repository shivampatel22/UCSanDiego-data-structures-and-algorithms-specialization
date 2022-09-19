"""queue implementation using linked list without tail.Enqueue -> pushBack(), Dequeue -> popFront()"""
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
    
    def pushBack(self, data):
        """pushes a new node at the end of the linked list.Iterate the list to reach end node
        and then point last node to new node."""
        newNode = Node(data)
        if self.head is None:
            "if the list is empty."
            self.head = newNode
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newNode
        temp = None
        return
        
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
    #llist.head = Node(1)
    #second = Node(2)
    #third = Node(3)
    #llist.head.next = second
    #second.next = third
    llist.pushBack(0)
    llist.pushBack(1)
    llist.popFront()
    llist.printList()
    