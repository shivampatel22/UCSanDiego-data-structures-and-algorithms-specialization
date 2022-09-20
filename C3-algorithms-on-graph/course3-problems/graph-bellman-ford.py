"""
bellman-ford algorithm
Time complexity = O(V.E)
Space complexity = O(V+E)
"""

import sys

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
    def initializeSingleSource(self, s):
        self.d = {}
        self.parent = {}
        inf = sys.maxsize
        for u in self.adj:
            self.d[u] = inf
            self.parent[u] = None
        self.d[s] = 0
    def relax(self, u, v, wt):
        if self.d[v] > self.d[u] + wt:
            self.d[v] = self.d[u] + wt
            self.parent[v] = u
    def bellmanFord(self, s):
        n = len(self.adj)
        self.initializeSingleSource(s)
        for i in range(n-1):
            for u in self.adj:
                for v in self.adj[u]:
                    self.relax(u,v,(self.adj[u])[v])
        for u in self.adj:
            for v in self.adj[u]:
                if self.d[v] > self.d[u] + (self.adj[u])[v]:
                    return False
        #print(self.adj)
        print (self.d)

if __name__ == '__main__':
    g = Graph()
    g.addEdge("A", "B", 7)
    g.addEdge("A", "D", 5)
    g.addEdge("B", "C", 8)
    g.addEdge("B", "D", 9)
    g.addEdge("B", "E", 7)
    g.addEdge("C", "E", 5)
    g.addEdge("D", "E", 15)
    g.addEdge("D", "F", 6)
    g.addEdge("E", "F", 8)
    g.addEdge("E", "G", 9)
    g.addEdge("F", "G", 11)
    g.bellmanFord("A")
                    
            
        
    
    
            
        
        
        
