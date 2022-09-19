"""deque in python"""
import collections
Dq = collections.deque([1,2,3])

def pushFront(x):
    Dq.appendleft(x)

def pushBack(x):
    Dq.append(x)

def getFront():
    if (Dq[0] is not None):
        return Dq[0]
    else:
        return -1

def popFront():
    if Dq:
        Dq.popleft()

def popBack():
    if Dq:
        Dq.pop()

if __name__ == '__main__':
    print(Dq)
    print("pushFront '0'")
    pushFront(0)
    print(*Dq)
    print("pushBack '4'")
    pushBack(4)
    print(*Dq)
    print("front -> {}".format(getFront()))
    print("poping front")
    popFront()
    print(*Dq)
    print("front -> {}".format(getFront()))
    
