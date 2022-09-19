"""implementation of circular linked list with tail only."""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CLinkedList():
    def __init__(self):
        self.tail = None
        
    def printList(self):
        temp = self.tail.next
        while(temp):
            print(temp.data)
            temp = temp.next
            if temp == self.tail.next:
                break
        temp = None
        return
        
    def pushFront(self, new_data):
        newNode = Node(new_data)
        if self.tail is None:
            newNode.next = newNode
            self.tail = newNode
            return
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            #print(self.tail.data)
            return
        
    def pushBack(self, new_data):
        newNode = Node(new_data)
        if self.tail is None:
            newNode.next = newNode
            self.tail = newNode
            return
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
            return
        
    def popFront(self):
        if self.tail is None:
            print("list empty.")
            return
        self.tail.next = self.tail.next.next
        return
    
    def popBack(self):
        if self.tail is None:
            print("list empty.")
            return
        temp = self.tail.next
        while(temp):
            temp = temp.next
            if temp.next == self.tail:
                break
        temp.next = self.tail.next
        self.tail = temp
        return
            
            
if __name__ == '__main__':
    cllist = CLinkedList()
    cllist.pushFront(3)
    cllist.pushFront(2)
    cllist.pushFront(1)
    cllist.pushBack(4)
    #cllist.popFront()
    cllist.popBack()
    cllist.printList()
    
            