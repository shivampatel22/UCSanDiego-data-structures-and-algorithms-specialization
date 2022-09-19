def knapsack_with_reps(W, val, wt, n):
    value = [0 for i in range(W+1)]
    #count = [0 for i in range(n+1)]
    for w in range(1, W+1):
        value[w] = 0
        for i in range(n):
            if wt[i] <= w:
                currVal = value[w-wt[i]] + val[i]
                if currVal > value[w]:
                    value[w] = currVal     
    print(value[W])
    print(value)
    
def knapsack_without_reps(W, val, wt, n):
    value  = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for w in range(1, W+1):
            value[i][w] = value[i-1][w]
            if wt[i-1] <= w:
                currVal = value[i-1][w-wt[i-1]] + val[i-1]
                if currVal > value[i][w]:
                    value[i][w] = currVal
    print (value[n][W])
    reconstruct(value, n, W, wt, val)
    
def reconstruct(value, n, W, wt, val):
    sol = [0 for i in range(n)]
    i = n
    j = W
    while i>0 and j>0:
        if value[i][j] == value[i-1][j]:
            sol[i-1] = 0
            i = i-1
        elif value[i][j] == value[i-1][j-wt[i-1]]+val[i-1]:
            sol[i-1] = 1
            j = j-wt[i-1]
            i = i-1
    print(sol)
if __name__ == '__main__':
    W = int(input())
    n = int(input())
    val = [int(x) for x in input().split()]
    wt = [int(x) for x in input().split()]
    #knapsack_with_reps(W,val,wt,n)
    knapsack_without_reps(W,val,wt,n)
    