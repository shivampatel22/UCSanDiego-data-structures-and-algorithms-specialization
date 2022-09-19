"""implementation of singly linked list without tail.All operations on the back of the
list take O(n) time."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
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
        
    def topFront(self):
        "returns the data/key at the first node.Return data at head"
        return self.head.data
        
    def popFront(self):
        "pops out the first node.Point head to the second node."
        self.head = self.head.next
        
    def remove(self, key):
        """removes/deletes any node with given key.Navigate list for the key and maintain info of previous node until
        a key is found or last node is reached.If found, point previos node to next node of current node."""
        temp = self.head
        if temp is not None:
            "if the list is not empty."
            if temp.data == key:
                "if the node to be removed is the first node."
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                print("key found and removed")
                break
            prev = temp
            temp = temp.next
        if (temp is None):
            "key is not in the list."
            print("key not found.")
            return
            
        prev.next = temp.next
        "updating previous node to point to the node next to the node to be removed."
        temp = None
        return
    
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
    
    def topBack(self):
        """returns last node data of the list."""
        if self.head is None:
            return "empty list."
        temp = self.head
        while(temp.next):
            temp = temp.next
        return temp.data
    
    def popBack(self):
        """pops out last node of the list."""
        if self.head is None:
            print("list empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None
        return
    
    def insertAfter(self, key, new_data):
        """inserts a node after a given node with given key."""
        newNode = Node(new_data)
        if self.head is None:
            self.head = newNode
            return
        if self.head.next is None:
            self.head.next = newNode
            return
        temp = self.head
        while(temp is not None):
            prev_node = temp
            if (temp.data == key):
                break
            temp = temp.next
        if temp is None:
            print("key not found.")
            return
        newNode.next = prev_node.next
        prev_node.next = newNode
        temp = None
        return
    
    def insertBefore(self, key, new_data):
        """inserts a node before a node with given key."""
        newNode = Node(new_data)
        if self.head is None:
            print("list empty.")
            return
        if self.head.next is None:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        while(temp is not None):
            if (temp.data == key):
                break
            prev_node = temp
            temp = temp.next
        if temp is None:
            print("key not found.")
            return
        newNode.next = prev_node.next
        prev_node.next = newNode
        temp = None
        return
    
    def findKey(self, key):
        if self.head is None:
            print("list empty.")
        temp = self.head
        while(temp):
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return False
        else:
            temp = None
            return True
        
            
        
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
    #llist.printList()
    #llist.remove(5)
    #llist.popFront()
    #print(llist.topFront())
    #llist.pushBack(4)
    #print(llist.topBack())
    #llist.popBack()
    #llist.insertAfter(2, 4)
    #llist.insertBefore(4, 3)
    #print(llist.isEmpty())
    print(llist.findKey(3))
    llist.printList()
    
    
    