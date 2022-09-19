def max_ad_profit(a, b, n):
    """Given two sequences a1,a2,...,an (ai is the profit per click of the i-th ad) and
    b1,b2,...,bn (bi is the average number of clicks per day of the i-th slot), we need 
    to partition them into n pairs (ai,bj) such that the sum of their products is maximized."""
    
    profit = 0
    while (len(a)):
        max_ad = max(a)
        max_slot = max(b)
        profit += max_slot * max_ad
        a.remove(max_ad)
        b.remove(max_slot)
        
    return profit
    
if __name__ == '__main__':
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    print(max_ad_profit(a, b, n))
    
        