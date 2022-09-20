#Uses python3
import sys


def acyclic(adj):
    
    visited_adj = [False] * len(adj)

    def dfs(vertex, cyclic=False):
        visited_adj[vertex], rec_visited[vertex] = True, True
        for adj_node in adj[vertex]:
            if not visited_adj[adj_node]:
                cyclic = dfs(adj_node, cyclic)
            elif rec_visited[adj_node]: 
                cyclic = True
        rec_visited[vertex] = False 
        return cyclic

    for index in range(len(visited_adj)):
        if not visited_adj[index]:
            rec_visited = [False] * len(visited_adj) 
            if dfs(index): 
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))