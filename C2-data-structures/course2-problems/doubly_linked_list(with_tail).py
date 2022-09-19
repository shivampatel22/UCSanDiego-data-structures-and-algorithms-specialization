"""imlementation of DLL with tail. All operations on front or end of the list take
O(1) time."""
class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def printList(self, dir = 'f'):
        if self.head is None:
            print("lsit emtpy.")
            return
        if dir == 'f':
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next    
        elif dir == 'b':
            temp = self.tail
            while(temp):
                print(temp.data)
                temp = temp.prev
        temp = None
        return
    
    def insertAfter(self, key, new_data):
        newNode = Node(new_data)
        if self.head is None:
            print("list empty.")
            return
        if self.head.next is None:
            if self.head == key:
                self.head.next = newNode
                newNode.prev = self.head
                self.tail = newNode
            return
        temp = self.head
        while(temp):
            prev_node = temp
            if(temp.data == key):
                break
            temp = temp.next
        if temp is None:
            print("node not found.")
            return
        if self.tail == prev_node:
            prev_node.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return
        newNode.next = prev_node.next
        prev_node.next.prev = newNode
        prev_node.next = newNode
        newNode.prev = prev_node
        temp = None
        return
    
    def insertBefore(self, key, new_data):
        newNode = Node(new_data)
        if self.head is None:
            print("lsit empty.")
            return
        if self.head.next is None:
            if self.head.data == key:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode   
            return
        temp = self.tail
        while(temp):
            curr_node = temp
            if(temp.data == key):
                break
            temp = temp.prev
        if temp is None:
            print("node not found.")
            return
        if self.head == curr_node:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode 
            return
        newNode.next = curr_node
        newNode.prev = curr_node.prev
        curr_node.prev.next = newNode
        curr_node.prev = newNode
        temp = None
        return
    
    def popBack(self):
        if self.head is None:
            print("list empty.")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        

if __name__ == '__main__':
    dllist = DLinkedList()
    dllist.head = Node(1)
    #dllist.tail = dllist.head
    second = Node(2)
    third = Node(3)
    dllist.head.next = second
    second.next = third
    dllist.tail = third
    third.prev = second
    second.prev = dllist.head
    dllist.printList()
    #dllist.printList('b')
    #dllist.insertAfter(3, 0)  
    dllist.insertBefore(1, 0)
    dllist.popBack()
    dllist.printList()
    
    
            
                
        