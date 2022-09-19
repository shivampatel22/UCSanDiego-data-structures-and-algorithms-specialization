"""disjoint set implementation"""

class disjointSet():
    def __init__(self, n):
        """makeset: create a forset of single node trees rooted at the same node"""
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def findSet(self, i):
        if i != self.parent[i]:
            """recursive two pass method for path compression"""
            self.parent[i] = self.findSet(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.findSet(i)
        j_id = self.findSet(j)
        if i_id == j_id:
            return
        """merging two trees of different ranks does not change the rank of the resulting tree"""
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
        """if ranks are equal then the rank of the resulting tree will be incremented by 1""" 
        if self.rank[i_id] == self.rank[j_id]:
            self.rank[j_id] = self.rank[j_id] + 1

if __name__ == '__main__':
    
    ds = disjointSet(9)
    print("start:")
    print(ds.parent)
    print(ds.rank)
    print("union (2,4)")
    ds.union(2,4)
    print(ds.parent)
    print(ds.rank)
    print("union (5,2)")
    ds.union(5,2)
    print(ds.parent)
    print(ds.rank)
    print("querry: set(4) == set(5): {}".format(ds.findSet(4)==ds.findSet(5)))
