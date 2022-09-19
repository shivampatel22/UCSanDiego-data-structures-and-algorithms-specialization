"""There are given N ropes of different lengths,
we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths.
The task is to connect the ropes with minimum cost.

in: 4 3 2 6
out: 29
in: 4 2 7 6 9
out: 62
"""

import heapq 

def minCost(arr,n):
    heapq.heapify(arr)
    tot_cost = 0
    while(len(arr) > 1):
        r1 = heapq.heappop(arr)
        r2 = heapq.heappop(arr)
        tot_cost += r1+r2
        heapq.heappush(arr, r1+r2)
    return tot_cost

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(minCost(arr,n))
