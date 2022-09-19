def power(m,n):
    if n == 1:
        return m
    if n%2 == 0:
        return(power(m*m, n/2))
    elif n%2 != 0:
        return(m * power(m*m, (n-1)/2))
        
m ,n = map(int, input().split())
print(power(m,n))