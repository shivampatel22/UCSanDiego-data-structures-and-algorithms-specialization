"""
Given an array A = [a0,a1,...,an−1], find
a longest increasing subsequence (LIS), i.e., ai1,ai2,...,aik such that i1 < i2 < ... < ik, ai1 < ai2 < ··· < aik, and k is maximal.
"""
import sys

def LIS(arr, N):
    sol = [None for i in range(N+1)]
    sol[0] = 0
    for i in range(1, N+1):
        sol[i] = 1
        for j in range(i):
            if arr[j] < arr[i-1]:
                curr_sol = sol[j+1] + 1
                if curr_sol > sol[i]:
                    sol[i] = curr_sol
    print(sol)
    return max(sol)
            

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]
    print(LIS(arr,N))
