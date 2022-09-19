"""sort stack using recursion"""
def sort(s):
    if not isEmpty(s):
        temp = s.pop()
        sort(s)
        insert(s,temp)
        
def insert(s,item):
    if isEmpty(s):
        s.append(item)
    else:
        if item > getTop(s):
            s.append(item)
        else:
            temp = s.pop()
            insert(s,item)
            s.append(temp)
        
def isEmpty(s):
    return len(s) == 0

def getTop(s):
    return s[-1]

def printStack(s):
    print(*s)
    
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    stack = []
    for e in arr:
        stack.append(e)
    sort(stack)
    printStack(stack)