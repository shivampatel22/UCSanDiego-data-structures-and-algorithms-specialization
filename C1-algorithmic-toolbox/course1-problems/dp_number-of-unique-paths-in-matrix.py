"""Given a M X N matrix with your initial position at the top-left cell,
find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.
possible moves:  | or -->
                 V
"""
def numWays(N,M):
    ways = [[0 for i in range(M)] for j in range(N)]
    ways[0][0] = 0
    for i in range(1,N):
        ways[0][i] = 1
    for i in range(1,M):
        ways[i][0] =  1
    for i in range(2,M):
        for j in range(2,N):
            ways[i][j] = ways[i-1][j] + ways[i][j-1]
    return ways[M-1][N-1]

if __name__ == '__main__':
    M, N = map(int, input().split())
    print(numWays(M, N))
