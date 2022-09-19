def knapsack_without_rep(W, w):
    res = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for wt in range(1, W+1):
            res[i][wt] = res[i-1][wt]
            if w[i-1] <= wt:
                val = res[i-1][wt - w[i-1]] + w[i-1]
                if val > res[i][wt]:
                    res[i][wt] = val

    return res[n][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    result = knapsack_without_rep(W, w)
    print(result)