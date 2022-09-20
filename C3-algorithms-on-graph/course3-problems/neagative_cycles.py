#Uses python3
import sys
import numpy as np

def negative_cycle(adj, cost):
    
    dist = {vertex: np.inf for vertex in range(len(adj))}
    neg_cycle = 0

    for index in range(len(adj)):
        for vertex in range(len(adj)):
            for adj_vertex in adj[vertex]:
                v_index = adj[vertex].index(adj_vertex)
                if dist[vertex] == np.inf:
                    dist[vertex] = 0
                updated_distance = dist[vertex] + cost[vertex][v_index]
                if updated_distance < dist[adj_vertex]:
                    dist[adj_vertex] = updated_distance
                    if index == len(adj) - 1:
                        neg_cycle = 1
    return neg_cycle


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))