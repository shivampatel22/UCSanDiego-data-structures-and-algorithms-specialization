"""bfs on graph"""
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
    def neighbors(self, u):
        return self.adj[u]
    def bfs(self, s):
        level = {}
        level[s] = 0
        parent = {}
        parent[s] = None
        frontier = [s]
        i = 0
        while frontier:
            next = []
            for u in frontier:
                for v in self.adj[u]:
                    if v not in level:
                        level[v] = i+1
                        parent[v] = u
                        next.append(v)
            frontier = next
            i += 1
        print("vertex to level map of every vertex reachable from %r" %s)
        print(level)
        print("parent pointers to every vertex reachable from %r" %s)
        print(parent)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    g.bfs(2)
