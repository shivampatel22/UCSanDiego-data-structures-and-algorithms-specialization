def EditDistanceDP(A,B):
    """min number of operations(insertion,deletion,substitution) required to convert A into B.
    O(mn) time, O(mn) space."""
    m = len(A)
    n = len(B)
    Edit = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        Edit[i][0] = 0
    for j in range(n+1):
        Edit[0][j] = 0
        
    for j in range(1,n+1):
        for i in range(1,m+1):
            if A[i-1] != B[j-1]:
                Edit[i][j] = 1 + min(Edit[i-1][j], Edit[i][j-1], Edit[i-1][j-1])
            else:
                Edit[i][j] = min(Edit[i-1][j]+1, Edit[i][j-1]+1, Edit[i-1][j-1])
    print(Edit)
    print(Edit[m][n])
    reconstruct(A, B, Edit, m, n)

def reconstruct(A, B, ED, i, j):
    """reconstructing an optimal sequence of operations. O(m+n) time."""
    alignment_A = []
    alignment_B = []
    while i>0 and j>0:
        if i>0 and ED[i][j] == ED[i-1][j]+1:
            alignment_A.append(A[i-1])
            alignment_B.append("-")
            i -= 1
        elif j>0 and ED[i][j] == ED[i][j-1]+1:
            alignment_A.append("-")
            alignment_B.append(B[j-1])
            j -= 1
        else:
            alignment_A.append(A[i-1])
            alignment_B.append(B[j-1])
            i -= 1
            j -= 1
    print([ele for ele in reversed(alignment_A)])
    print([ele for ele in reversed(alignment_B)])        
        

if __name__ == '__main__':
    A = input()
    B = input()
    EditDistanceDP(A,B)