"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        self.makeEqual(l1, l2)
        prev = None
        carry = 0
        while(l1 is not None):
            node = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry) // 10
            if prev is not None:
                prev.next = node
            else:
                head = node
            prev = node
            l1 = l1.next
            l2 = l2.next
        if carry != 0:
            node = ListNode(1)
            prev.next = node
        return head
            
    def makeEqual(self, l1, l2):
        while (l1.next is not None) and (l2.next is not None):
            l1 = l1.next
            l2 = l2.next
        if l1.next == None:
            while(l2.next is not None):
                node = ListNode(0)
                l1.next = node
                l1 = l1.next
                l2 = l2.next
        elif l2.next == None:
            while(l1.next is not None):
                node = ListNode(0)
                l2.next = node
                l1 = l1.next
                l2 = l2.next
        
    
        
        
        
