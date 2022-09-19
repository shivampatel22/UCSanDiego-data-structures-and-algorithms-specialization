"""reverse a stack using recursion"""
def reverse(s):
    if not isEmpty(s):
        temp = s.pop()
        reverse(s)
        insert(s,temp)
        
def insert(s,item):
    if isEmpty(s):
        s.append(item)
    else:
        temp = s.pop()
        insert(s,item)
        s.append(temp)
        
def isEmpty(s):
    return len(s) == 0

def printStack(s):
    print(*s)
    
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    stack = []
    for e in arr:
        stack.append(e)
    reverse(stack)
    printStack(stack)