import sys
sys.setrecursionlimit(10**8)
def lastdigit_fibo(n):
    memo = [None]*(n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = (memo[i-1] + memo[i-2])%10
    return(memo[n])
    
if __name__ == '__main__':    
    n = int(input())
    print(lastdigit_fibo(n))    