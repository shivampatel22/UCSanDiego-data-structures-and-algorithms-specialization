memo = {0:0, 1:1}
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
    
if __name__ == '__main__':    
    n = int(input())
    print(fibo(n))    