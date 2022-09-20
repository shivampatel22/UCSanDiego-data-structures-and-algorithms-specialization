"""graph representation as adjacency matrix"""

import sys

class graph(object):
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[-1 for x in range(self.numVertices)] for y in range(self.numVertices)]
        self.keyToVert = {} 
        self.vertList = [-1 for x in range(self.numVertices)]

    def setVertex(self, vertNum, key):
        if 0 <= vertNum <= vertNum:
            self.keyToVert[key] = vertNum
            self.vertList[vertNum] = key

    def setEdge(self, frm, to, wt=0):
        f = self.keyToVert[frm]
        t = self.keyToVert[to]
        self.adjMatrix[f][t] = wt
        self.adjMatrix[t][f] = wt

    def getVert(self):
        return self.vertList

    def getEdges(self):
        self.edges = []
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.adjMatrix[i][j] != -1:
                    self.edges.append((self.vertList[i], self.vertList[j]))
        return self.edges
    
    def getadjMatrix(self):
        return self.adjMatrix

G = graph(6)
G.setVertex(0,'a')
G.setVertex(1,'b')
G.setVertex(2,'c')
G.setVertex(3,'d')
G.setVertex(4,'e')
G.setVertex(5,'f')
G.setEdge('a','e',10)
G.setEdge('a','c',20)
G.setEdge('c','b',30)
G.setEdge('b','e',40)
G.setEdge('e','d',50)
G.setEdge('f','e',60)
print("Vertices of Graph")
print(G.getVert())
print("Edges of Graph")
print(G.getEdges())
print("Adjacency Matrix of Graph")
print(G.getadjMatrix())
        
