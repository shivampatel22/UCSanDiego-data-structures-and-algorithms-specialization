def distPrize(n):
    """You are organizing a funny competition for children. As a prize fund you have n candies.
    You would like to use these candies for top k places in a competition with a natural
    restriction that a higher place gets a larger number of candies. To make as many children 
    happy as possible, you are going to find the largest value of k for which it is possible."""

    prize = []
    k = 1
    dist_candies = 1
    #print(k, end = " ")
    if n-dist_candies >= 0:
        while True:
            if n-dist_candies <= k:
                break
            prize.append(k)
            k += 1
            dist_candies += k
            
        #print(k)   
        prize.append(n-(dist_candies-k))
    print(len(prize))
    for p in prize:
        print(p, end = " ")
        
if __name__ == '__main__':
    n = int(input())
    distPrize(n)
    