"""Given a sorted deck of cards numbered 1 to N.

1) We pick up 1 card and put it on the back of the deck.

2) Now, we pick up another card , it turns out to be card numbered 1 , we put it outside the deck.

3) Now we pick up 2 cards and put it on the back of the deck.

4) Now, we pick up another card and it turns out to be card numbered 2 , we put it outside the deck. ...

We perform this step till the last card.
if such arrangement of decks is possible, output the arrangement, if it is not possible for a particular value of N then output -1.
in: 4
out: 2 1 4 3 """

import collections

def enqueue(Dq, elem):
    Dq.appendleft(elem)

def dequeue(Dq):
    return(Dq.pop())

if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        Dq = collections.deque([N])
        for i in range(N-1, 0, -1):
            enqueue(Dq, i)
            for j in range(i):
                enqueue(Dq, dequeue(Dq))
        print(*Dq)
                   
        
