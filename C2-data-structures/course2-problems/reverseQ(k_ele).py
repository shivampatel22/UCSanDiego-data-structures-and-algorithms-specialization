"""reverse first k elements of a queue. O(n) time and O(n) space"""
def reverseK(queue,k,n):
    stack = []
    for i in range(k):
        stack.append(queue.pop(0))
    #print(stack)
    while(stack):
        queue.append(stack.pop())
    for i in range(n-k):
        queue.append(queue.pop(0))
    return queue
    


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*reverseK(queue,k,n))
