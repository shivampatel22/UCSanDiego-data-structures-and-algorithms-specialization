import sys
def recursiveCoinChange(coins, money):
    if money == 0:
        return 0
    minNumCoins = sys.maxsize
    for coin in coins:
        if coin <= money:
            numCoins = recursiveCoinChange(coins, money-coin)
            if (numCoins+1) < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins

def DP_coinChange(coins, money):
    minNumCoins = [None]*(money+1)
    minNumCoins[0] = 0
    for m in range(1,money+1):
        minNumCoins[m] = sys.maxsize
        for coin in coins:
            if m >= coin:
                numCoins = minNumCoins[m-coin] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[m]


if __name__ == '__main__':
    money = int(input())
    coins = [int(x) for x in input().split()]
#    print(recursiveCoinChange(coins, money))
#    print(DP_coinChange(coins, money))

    