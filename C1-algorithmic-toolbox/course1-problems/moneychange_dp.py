def moneychange_dp(money, coins):
    min_coins = [0] * (money+1)
    min_coins[0] = 0
    for m in range(1, money+1):
        min_coins[m] = m
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_coins[m - coins[i]] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]
    
if __name__ == '__main__':
    money = int(input())
    coins = [1, 3, 4]
    print(moneychange_dp(money, coins))
    