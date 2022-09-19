"""Given an array A of size N having distinct elements,
the task is to find the next greater element for each element of the array in order of their appearance in the array.
If no such element exists, output -1.

in: 1 3 2 4
out: 3 4 4 -1
in: 4 3 2 1
out: -1 -1 -1 -1

"""

def NGE(arr, n):
    stack = []
    nge = {}
    for i in range(n):
        nge[arr[i]] = -1
    stack.append(arr[0])
    i = 1
    
    while i < n:
        
        while i<n and stack[-1]>arr[i]:
            stack.append(arr[i])
            i += 1
        if i == n:
            break
        
        #cnt = 0
        while (len(stack)>0 and i<n) and stack[-1]<arr[i]:
            e = stack.pop()
            
            #cnt += 1
            nge[e] = arr[i]
        if i == n:
            i -= 1
        stack.append(arr[i])
        i += 1
    arr_nge = []
    for i in range(n):
        arr_nge.append(nge[arr[i]])
    return arr_nge
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*NGE(arr,n))
