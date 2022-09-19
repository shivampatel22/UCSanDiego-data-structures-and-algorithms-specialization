def fractional_knapsack(W, w, V, n):
    """A thief finds much more loot than his bag can fit. Help him to find the most 
    valuable combination of items assuming that any fraction of a loot item can be 
    put into his bag.  Output the maximal value of fractions of items that fit into
    the knapsack. The absolute value of the difference between the answer of your program
    and the optimal value should be at most 10−3. To ensure this, output your answer 
    with at least four digits after the decimal point (otherwise your answer, while 
    being computed correctly, can turn out to be wrong because of rounding issues)."""

    current_W = 0
    unit_value = {}
    max_v = 0
    
    for i in range(n):
        unit_value[V[i]/w[i]] = w[i]
    #print(unit_value)
    unit_value_S = sorted(unit_value.keys(), reverse = True)
    #print(unit_value_S)
    
    for elem in unit_value_S:
        if current_W == W:
            return max_v
        else:
            a = min(W - current_W, unit_value[elem])
            max_v += elem * a
            current_W += a
    return max_v
    
if __name__ == '__main__':
    n, W = map(int, input().split())
    w = [0] * n 
    V = [0] * n
    for i in range(n):
        V[i], w[i] = map(int, input().split())
    print('%.4f'%(fractional_knapsack(W, w, V, n)))
        
    
        