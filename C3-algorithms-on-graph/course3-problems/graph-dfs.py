"""dfs on graph"""
class Graph(object):
    def __init__(self, typ = "undirected"):
        self.adj = {}
        self.type = typ
    def addVertex(self, u):
        if u not in self.adj:
            self.adj[u] = set()
        else:
            return "vertex already in graph"
    def addEdge(self, u, v):
        if u not in self.adj:
            self.addVertex(u)
        self.adj[u].add(v)
        if v not in self.adj:
            self.addVertex(v)
        if self.type == "undirected":
            self.adj[v].add(u)
    def dfs(self):
        self.visited = {}
        self.parent = {}
        self.order = []
        self.prepost = {}
        self.clock = 0
        for u in self.adj:
            self.visited[u] = False
            self.parent[u] = None
            self.prepost[u] = [0,0]
        for u in self.adj:
            if not self.visited[u]:
                self.order.append(u)
                self.dfsVisit(u)
        print(self.order)
        print(self.prepost)
    def dfsVisit(self, u):
        self.previsit(u)
        self.visited[u] = True
        for v in self.adj[u]:
            if not self.visited[v]:
                self.order.append(v)
                self.parent[v] = u
                self.dfsVisit(v)
        self.postvisit(u)
    def previsit(self, u):
        self.clock += 1
        self.prepost[u][0] = self.clock
    def postvisit(self, u):
        self.clock += 1
        self.prepost[u][1] = self.clock

if __name__ == '__main__':
    g = Graph()
    g.addEdge('a', 'b')
    g.addEdge('b', 'c')
    g.addEdge('c', 'a')
    g.addEdge('a', 'd')
    g.dfs()
    
