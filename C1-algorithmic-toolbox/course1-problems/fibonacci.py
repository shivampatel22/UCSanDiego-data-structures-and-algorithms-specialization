def fibRec(n):
    """TIME COMPLEXITY : O(2^n), SPACE COMPLEXITY : O(n)"""
    if n <= 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)
    
def fibItr(n):
    """TIME COMPLEXITY : O(n), SPACE COMPLEXITY : O(1)"""
    t0 = 0
    t1 = 1
    if n == 0:
        return t0
    elif n == 1:
        return t1
    for i in range(2,n+1):
        t2 = t1 + t0
        t0 = t1
        t1 = t2    
    return t2

def fibDP(n):
    """TIME COMPLEXITY : O(n)/O(n^2) for large numbers, SPACE COMPLEXITY : O(n)"""
    memo = [None] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fibPOM(n):
    """TIME COMPLEXITY : O(n), SPACE COMPLEXITY : O(1)"""
    F = [[1,1], 
         [1,0]]
    if n == 0:
        return 0
    if n == 1:
        return F[0][0]
    
    M = [[1,1],
         [1,0]]
    
    for i in range(2,n):
        m00 = (F[0][0] * M[0][0]) + (F[0][1] * M[1][0])
        m01 = (F[0][0] * M[0][1]) + (F[0][1] * M[1][1])
        m10 = (F[1][0] * M[0][0]) + (F[1][1] * M[1][0])
        m11 = (F[1][0] * M[0][1]) + (F[1][1] * M[1][1]) 
    
        F[0][0] = m00
        F[0][1] = m01
        F[1][0] = m10
        F[1][1] = m11
    return F[0][0]

def fibFast(n):
    """TIME COMPLEXITY : O(logn), SPACE COMPLEXITY : O(logn)"""
    memo = [0]*10000
    if n == 0:
        return 0
    elif n <= 2:
        memo[n] = 1
        return 1
    if (memo[n]):
        return memo[n]
    if (n & 1):
        k = (n+1) // 2
    else:
        k = n // 2
    if (n & 1):
        memo[n] = (fibFast(k) * fibFast(k)) + (fibFast(k-1) * fibFast(k-1))
    else:
        memo[n] = (fibFast(k) * fibFast(k)) + (2*fibFast(k-1)*fibFast(k))
    return memo[n]
        
        
if __name__ == '__main__':
    n = int(input())
    print("fibonacci using recursion\n" + str(fibRec(n)))
    print("fibonacci using iteration\n" + str(fibItr(n)))
    print("fibonacci using dp\n" + str(fibDP(n)))
    print("fibonacci using power of matrix\n" + str(fibPOM(n)))
    print("fibonacci using matrix reduction\n" + str(fibFast(n)))
    