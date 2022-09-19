def coinChangeCount(coins, m, money):
    if money == 0:
        return 1
    if money < 0:
        return 0
    if (money>0 and m<=0):
        return 0
    return coinChangeCount(coins, m, money-coins[m-1]) + coinChangeCount(coins, m-1, money)


def coinChangeCountDP(coins, money):
    numWays = [0]*(money+1)
    numWays[0] = 1
    for coin in coins:
        for m in range(money+1):
            if coin <= m:
                numWays[m] += numWays[m-coin]
    print(numWays)
    return (numWays[money])
    

if __name__ == '__main__':
    money = int(input())
    coins = [int(x) for x in input().split()]
    #print(coinChangeCount(coins, len(coins), money))
    print(coinChangeCountDP(coins, money))