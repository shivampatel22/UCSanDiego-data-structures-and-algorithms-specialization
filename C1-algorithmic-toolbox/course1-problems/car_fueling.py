def carFueling(m, n, stops_new):
    """You are going to travel to another city that is located d miles away from your 
    home city. Your car can travel at most m miles on a full tank and you start with a 
    full tank. Along your way, there are gas stations at distances stop1,stop2,...,stopn 
    from your home city. What is the minimum number of refills needed."""
    
    numRefills = 0
    currentstop = 1
    lastRefill = 0
    while currentstop <= n+1:
        lastRefill = currentstop - 1
        while((currentstop <= n+1) and (stops_new[currentstop] - stops_new[lastRefill] <= m)):
            currentstop += 1
            if currentstop > n+1:
                break
        if currentstop-lastRefill == 1:
            return -1
        if currentstop <= n+1:
            numRefills += 1
    return numRefills
   
if  __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [0] * n
    stops_new = [0] * (n+1)
    
    
    stops = [int(stops) for stops in input().split()]
    for i in range(n):
        stops_new[i+1] = stops[i]
    stops_new.append(d)
    print(carFueling(m, n, stops_new))
    
    