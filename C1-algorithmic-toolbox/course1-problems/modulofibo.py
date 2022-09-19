def modfibo(n, m):
    """Given two integers n and m, output Fn mod m 
    (that is, the remainder of Fn when divided by m). """
    period = [None]*(2)
    period[0] = 0
    period[1] = 1
    flag = 0
    current = m
    for i in range(2,n+1):
       
        period.append((period[i-1] + period[i-2])%m)
        if period[i] == 0:
            flag = 1
        elif flag == 1 and period[i] != 1:
            flag = 0
        if flag == 1 and period[i] == 1:
            current = i-1
            break
   
    #print(period)
    if n == m:
        return period[-1]
    else:
        rem = n%current
        return(period[rem])
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(modfibo(n, m))
            