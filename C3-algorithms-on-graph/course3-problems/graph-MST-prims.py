"""Prim's algorithm for Minimum Spanning Tree problem"""
import sys, math, heapq

class Graph(object):
    def __init__(self):
        self.adj = {}

    def addVertex(self, u):
        if u not in self.adj:
            self.adj[u] = {}
        else:
            print("vertex already in graph")

    def addEdge(self, u, v, wt):
        if u not in self.adj:
            self.addVertex(u)
        (self.adj[u])[v] = wt
        if v not in self.adj:
            self.addVertex(v)
        (self.adj[v])[u] = wt

    def initialize(self, r):
        self.key = {}
        self.parent = {}
        self.inQ = {}
        inf = sys.maxsize
        for u in self.adj:
            self.key[u] = inf
            self.parent[u] = None
            self.inQ[u] = True
        self.key[r] = 0
        
    def mstPrim(self, r):
        self.initialize(r)
        self.Q = [(self.key[r], r)]
        self.cost = 0
        while(len(self.Q)):
            key, u = heapq.heappop(self.Q)
            if self.inQ[u] == True:
                self.inQ[u] = False
                self.cost = self.cost + key
                #print(u)
                for v in self.adj[u]:
                    if self.inQ[v] == True and self.key[v] > (self.adj[u])[v]:
                        self.parent[v] = u
                        self.key[v] = (self.adj[u])[v]
                        heapq.heappush(self.Q, (self.key[v], v))
            else:
                continue
        #print(self.adj)
        return self.cost

if __name__ == '__main__':
    g = Graph()
    g.addEdge("a", "b", 4)
    g.addEdge("a", "h", 8)
    g.addEdge("b", "h", 11)
    g.addEdge("b", "c", 8)
    g.addEdge("c", "i", 2)
    g.addEdge("c", "f", 4)
    g.addEdge("c", "d", 7)
    g.addEdge("i", "h", 7)
    g.addEdge("i", "g", 6)
    g.addEdge("g", "h", 1)
    g.addEdge("g", "f", 2)
    g.addEdge("d", "f", 14)
    g.addEdge("d", "e", 9)
    g.addEdge("e", "f", 10)
    print(g.mstPrim("a"))
    
