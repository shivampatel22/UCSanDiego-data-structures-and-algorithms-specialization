class PriorityQ():
    def __init__(self,maxSize):
        self.size = 0
        self.maxSize = maxSize
        self.H = [-10000]*(self.maxSize)
        
    def getLeftChild(self,index):
        return ((2*index) + 1)
    def getRightChild(self,index):
        return ((2*index)+2)
    def getParent(self,index):
        return ((index-1)//2)
    
    def shiftUp(self, i):
        #print("1")
        #print(parent)
        while (i > 0) and (self.H[i] > self.H[self.getParent(i)]):
            #print("1")
            self.H[i],self.H[self.getParent(i)] = self.H[self.getParent(i)],self.H[i]
            i = self.getParent(i)
    def shiftDown(self, i):
        maxIndex = i
        l = self.getLeftChild(i)
        if (i<=self.size) and (self.H[l] > self.H[maxIndex]):
            maxIndex = l
        r = self.getRightChild(i)
        if (i<=self.size) and (self.H[r] > self.H[maxIndex]):
            maxIndex = r
        if i != maxIndex:
            self.H[i],self.H[maxIndex] = self.H[maxIndex],self.H[i]
            self.shiftDown(maxIndex)

    def insert(self,p):
        if self.size == self.maxSize:
            print("Queue is full")
            return
        #self.size = self.size+1
        self.H[self.size] = p
        self.shiftUp(self.size)
        self.size = self.size+1
    def extractMax(self):
        result = self.H[0]
        self.H[0] = self.H[self.size-1]
        self.size = self.size - 1
        self.shiftDown(0)
        return result
    def remove(self,i):
        self.H[i-1] = self.H[0]+1
        self.shiftUp(i-1)
        self.extractMax()
    def changePriority(self,i,new_p):
        old_p = self.H[i-1]
        self.H[i-1] = new_p
        if new_p>old_p:
            self.shiftUp(i-1)
        else:
            self.shiftDown(i-1)
    def display(self):
         print(self.H)
         
if __name__ == '__main__':
    pq = PriorityQ(20)
    pq.insert(14)
    pq.insert(29)
    pq.insert(18)
    pq.insert(42)
    pq.insert(18)
    pq.insert(12)
    pq.insert(11)
    pq.insert(13)
    print("size = {}".format(pq.size))
    print("max element= {}".format(pq.extractMax()))
    print("size = {}".format(pq.size))
    pq.remove(7)
    pq.changePriority(1,42)
    pq.display()
    
        
        