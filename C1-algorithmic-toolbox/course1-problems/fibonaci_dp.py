def fibonacci(n):
    fiblist = [0] * (n+1)
    fiblist[0] = 0
    fiblist[1] = 1
    for i in range(2,n+1):
        fiblist[i] = fiblist[i-1] + fiblist[i-2]
        
    return(fiblist[n])
    
n = int(input())
print(fibonacci(n))