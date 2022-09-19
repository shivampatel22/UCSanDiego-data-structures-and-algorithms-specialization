"""linked list implementation with head and tail.All operations on the end of the list(except 
popBack()) take O(1) time."""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def printList(self):
        if self.head is None:
            print("empty list.")
            return
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        temp = None
        return
    
    def pushBack(self, new_data):
        newNode = Node(new_data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        temp = self.tail
        temp.next = newNode
        self.tail = newNode 
        temp = None
        return
    
    def popBack(self):
        if self.head is None:
            print("list empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        temp = self.head 
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        self.tail = prev
        temp = None
        return
            
    def topBack(self):
        print(self.tail.data)
        
  
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.tail = third
    llist.head.next = second
    second.next = third
    llist.pushBack(4)
    llist.popBack()
    llist.topBack()
    llist.printList()
    