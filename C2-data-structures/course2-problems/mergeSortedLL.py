class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addToTheLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode
            
            
    def mergeSort(self,head):
        if head == None or head.next == None:
            return head
        mid = self.getMiddle(head)
        nextNode = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nextNode)
        sortedLL = self.sortedMerge(left,right)
        return sortedLL
        
    def getMiddle(self,h):
        if h is None:
            return h
        slow = h
        fast = h
        while((fast.next is not None) and (fast.next.next is not None)):
            slow = slow.next
            fast = fast.next.next
        return slow
            
    def sortedMerge(self, head_a, head_b):
        dummyNode = Node(0)
        tail = dummyNode
        if head_a is None:
            tail.next = head_b
        if head_b is None:
            tail.next = head_a
        
        while head_a and head_b:
            if head_a.data < head_b.data:
                tail.next = head_a
                head_a = head_a.next
            else:
                tail.next = head_b
                head_b = head_b.next
            tail = tail.next
        if head_a is not None:
            tail.next = head_a
        if head_b is not None:
            tail.next = head_b
        
        return dummyNode.next

def printList(h):
        "prints the list."
        temp = h
        while(temp):
            print(temp.data)
            temp = temp.next
    
            
if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
   
    llist = LinkedList()
    
    for i in range(n):
        llist.addToTheLast(arr[i])
    print("ll:")
    printList(llist.head)
    
    H = llist.mergeSort(llist.head)
    
    print("sorted")
    printList(H)