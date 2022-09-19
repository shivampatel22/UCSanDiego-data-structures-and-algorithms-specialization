def REC_LCS(X, Y, m, n): 
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + REC_LCS(X, Y, m-1, n-1); 
    else: 
       return max(REC_LCS(X, Y, m, n-1), REC_LCS(X, Y, m-1, n)); 
   
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    print(c)
    print (c[m][n])
    reconstruct(X,m,n,c)

def reconstruct(X, i, j, c):
    if i==0 or j==0:
        return
    if c[i][j] == c[i-1][j-1]+1:
        reconstruct(X, i-1, j-1, c)
        print(X[i-1],end="")
    elif c[i][j] == c[i-1][j]:
        reconstruct(X, i-1, j, c)
    else:
        reconstruct(X, i, j-1, c)
if __name__ == '__main__':
   X = input()
   Y = input()
   LCS(X,Y)