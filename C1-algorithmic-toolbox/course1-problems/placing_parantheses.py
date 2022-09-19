import sys

def operator(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        assert False
        

def maximum_value(expression):
    for i in range(len(d)):
        maximum[i][i] = d[i]
        minimum[i][i] = d[i]
        
    for k in range(0, len(d)):
        for i in range(0, len(d) - k - 1):
            j = i + k + 1
            min_value, max_value = min_max_value(i, j)
            maximum[i][j] = max_value
            minimum[i][j] = min_value
            

def min_max_value(i, j):
    min_value = sys.maxsize
    max_value = -sys.maxsize
    for k in range(i, j):
        a = operator(maximum[i][k], maximum[k+1][j], ops[k])
        b = operator(maximum[i][k], minimum[k+1][j], ops[k])
        c = operator(minimum[i][k], maximum[k+1][j], ops[k])
        d = operator(minimum[i][k], minimum[k+1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


if __name__ == "__main__":
    expression = input()
    d = list(map(int, expression[0::2]))
    ops = list(expression[1::2])
    minimum = [[0 for i in range(len(d))] for j in range(len(d))]
    maximum = [[0 for i in range(len(d))] for j in range(len(d))]
    maximum_value(expression)
    print(maximum[0][len(d) - 1])
