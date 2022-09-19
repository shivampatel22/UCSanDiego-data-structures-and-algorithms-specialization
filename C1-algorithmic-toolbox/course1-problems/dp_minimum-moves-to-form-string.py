"""
Given a string S, we need to write a program to check if it is possible to construct the given string S by performing any of the below operations
any number of times. In each step, we can:

1.Add any character at the end of the string.
2.or, append the string to the string itself.
The above steps can be applied any number of times. We need to print the minimum steps required to form the string.
"""
import sys
def minMoves(S, n):
    moves = [None]*(n+1)
    moves[0] = 0
    moves[1] = 1
    for i in range(2, n+1):
        sol1 = sys.maxsize
        sol2 = sys.maxsize
        sol1 = moves[i-1] + 1
        num = i/2
        if abs(int(num)-num) == 0:
            if S[:int(num)] == S[int(num):i]:
                sol2 = moves[int(num)] + 1
        moves[i] = min(sol1, sol2)
    print(moves)
    return moves[n]

if __name__ == '__main__':
    S = input()
    print(minMoves(S,len(S)))
        
