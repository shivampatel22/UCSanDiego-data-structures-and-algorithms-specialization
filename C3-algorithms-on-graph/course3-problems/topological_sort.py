#Uses python3
import sys


def toposort(adj):
    
    visited = [False] * len(adj)
    order = list()

    def dfs(vertex):
        visited[vertex] = True
        for adj_vertex in adj[vertex]:
            if not visited[adj_vertex]:
                dfs(adj_vertex)
        order.append(vertex)

    for node in range(len(visited)):
        if not visited[node]:
            dfs(node)

    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')