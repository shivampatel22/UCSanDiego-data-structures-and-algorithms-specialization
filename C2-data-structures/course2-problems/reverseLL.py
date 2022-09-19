class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def my_reverse(self):
        prev1 = self.head.next
        prev2 = self.head.next.next
        temp = self.head.next.next.next
        prev1.next = self.head
        self.head.next = None
        cnt = 1
        while(temp):
            if cnt%2 != 0:
                prev2.next = prev1
                prev1 = temp
            else:
                prev1.next = prev2
                prev2 = temp
            
            temp = temp.next
            cnt += 1
        if (cnt%2==0):
            prev1.next = prev2
            self.head = prev1
        else:
            prev2.next = prev1
            self.head = prev2
        return 
    
    def nicks_reverse(self):
        prev = None
        
        while(self.head!=None):
            next_node = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next_node
        self.head = prev
        return
    
    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode
    
    def printList(self):
        "prints the list."
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
def intersetPoint(h_a,h_b):
    temp1 = h_a
    temp2 = h_b
#    print("list:")
#    while(temp1):
#        print(temp1.data)
#        temp1 = temp1.next
#    while(temp2):
#        print(temp2.data)
#        temp2 = temp2.next
    if temp1.data != temp2.data:
        return -1
    else:
        while(temp1.data == temp2.data):
            poi = temp1.data
            temp1 = temp1.next
            temp2 = temp2.next
        
    return poi
            
if __name__ == '__main__':
    n1,n2 = map(int,input().split())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    llist1 = LinkedList()
    llist2 = LinkedList()
    for i in range(n1):
        llist1.append(arr1[i])
    for i in range(n2):
        llist2.append(arr2[i])
    print("l1:")
    llist1.printList()
    print("l1:")
    llist2.printList()
    llist1.reverse()
    llist2.reverse()
    #llist.printList()
    print(intersetPoint(llist1.head,llist2.head))
        