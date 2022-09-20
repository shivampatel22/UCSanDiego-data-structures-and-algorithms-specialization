import sys, heapq

class Graph(object):
    def __init__(self):
        self.adj = {}
    def addVertex(self, u):
        if u not in self.adj:
            self.adj[u] = {}
        else:
            return "vertex already present in graph"
    def addEdge(self, u, v, wt):
        if u not in self.adj:
            self.addVertex(u)
        (self.adj[u])[v] = wt
        if v not in self.adj:
            self.addVertex(v)
    def initializeSingleSource(self, s):
        inf = sys.maxsize
        self.d = {}
        self.parent = {}
        for u in self.adj:
            self.d[u] = inf
            self.parent[u] = None
        self.d[s] = 0
    def relax(self, u, v, w):
        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.parent[v] = u
            heapq.heappush(self.Q, (self.d[v], v))
    def printPath(self, src, dst):
        def reconstruct(dst):
            if dst == src:
                print(src)
            else:
                reconstruct(self.parent[dst])
                print(dst)
        reconstruct(dst)
    def dijkstra(self, s):
        self.initializeSingleSource(s)
        self.S = set()
        self.Q = [(self.d[s], s)]
        while(len(self.Q)):
            dist, u = heapq.heappop(self.Q)
            self.S.add(u)
            for v in self.adj[u]:
                self.relax(u, v, (self.adj[u])[v])
        print(self.d)
        self.printPath(s, "E")

if __name__ == "__main__":
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
    g.dijkstra("A")
    #g.dijkstra("F")
        
        
            
