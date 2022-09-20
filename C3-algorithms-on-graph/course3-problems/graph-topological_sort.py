"""cycle detection and topological sort"""
class Graph(object):
    def __init__(self):
        self.adj = {}
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
    def dfs(self):
        self.visited = {}
        self.prepost = {}
        self.clock = 0
        self.color = {}
        for u in self.adj:
            self.visited[u] = False
            self.prepost[u] = [0,0]
            self.color[u] = "white"
        for u in self.adj:
            if not self.visited[u]:
                self.dfsVisit(u)
        print(self.prepost)
    def dfsVisit(self, u):
        self.visited[u] = True
        self.color[u] = "gray"
        self.previsit(u)
        for v in self.adj[u]:
            if not self.visited[v]:
                self.dfsVisit(v)
            if self.color[v] == "gray":
                self.isDag = False
        self.postvisit(u)
        self.color[u] = "black"
        self.linearOrder.append(u)
    def previsit(self, u):
        self.clock += 1
        self.prepost[u][0] = self.clock
    def postvisit(self, u):
        self.clock += 1
        self.prepost[u][1] = self.clock
    def topSort(self):
        self.linearOrder = []
        self.isDag = True
        self.dfs()
        if (self.isDag): 
            self.dfs()
            print(self.linearOrder)
        else:
            print("not a dag")

if __name__ == '__main__':
    g = Graph() 
    g.addEdge(5, 2); 
    g.addEdge(0, 5); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 0);
    g.topSort()
            
            
            
