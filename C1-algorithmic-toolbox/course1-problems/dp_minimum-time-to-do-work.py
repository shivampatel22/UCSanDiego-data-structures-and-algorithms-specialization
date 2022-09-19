"""
Given time taken by n tasks. Find the minimum time needed to finish the tasks such that skipping of tasks is allowed,
but can not skip two consecutive tasks.
"""
import sys

def minTime(arr, N):
    do = [0 for i in range(N+1)]
    skip = [0 for i in range(N+1)]

    do[1] = arr[0]
    skip[1] = 0

    for i in range(2, N+1):
        do[i] = min(do[i-1], skip[i-1]) + arr[i-1]
        skip[i] = do[i-1]

    return min(do[N], skip[N])

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]
    print(minTime(arr,N))
