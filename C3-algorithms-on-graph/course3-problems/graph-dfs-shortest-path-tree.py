"""breadht frst trees/shortest path trees/distance between 2 vertices"""
class Graph(object):
    def __init__(self, typ = "undirected"):
        self.adj = {}
        self.type = typ
    def addVertex(self, u):
        if u not in self.adj:
            self.adj[u] = set()
        else:
            return "vertex already present in graph"
    def addEdge(self, u, v):
        if u not in self.adj:
            self.addVertex(u)
        self.adj[u].add(v)
        if v not in self.adj:
            self.addVertex(v)
        if self.type == "undirected":
            self.adj[v].add(u)
    def bfs(self, s):
        self.parent = {}
        self.dist = {}
        self.parent[s] = None
        self.dist[s] = 0
        self.frontier = [s]
        i = 1
        while(self.frontier):
            self.next = []
            for u in self.frontier:
                for v in self.adj[u]:
                    if v not in self.dist:
                        self.dist[v] = i
                        self.parent[v] = u
                        self.next.append(v)
            self.frontier = self.next
            i += 1
    def pathAndDist(self,s,v):
        self.bfs(s)
        def printPath(v):
            if v == None:
                return 
            printPath(self.parent[v])
            print(v)
            
        if v not in self.parent:
            print("no path from {} to {} exists".format(s,v))
        else:
            print("distance of {} from {} is {}".format(v,s,self.dist[v]))
            print("path of {} from {}".format(v,s))
            printPath(v)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    g.pathAndDist(0,3)    
            
