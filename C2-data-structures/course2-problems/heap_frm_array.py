class heapBuilder:
  def __init__(self):
    self.swaps = []
    self.data = []
    
  def readData(self):
    global n
    n = int(input())
    self.data = [int(s) for s in input().split()]
    assert n == len(self.data)
    
  def writeResponse(self):
    print(len(self.swaps))
    for swap in self.swaps:
      print(swap[0], swap[1])
      
  def siftDown(self, i):
      minIndex = i
      left = 2 * i + 1
      if left < n and self.data[left] < self.data[minIndex]:
          minIndex = left
      right = 2 * i + 2
      if right < n and self.data[right] < self.data[minIndex]:
          minIndex = right
      if i != minIndex:
          self.data[i], self.data[minIndex] = self.data[minIndex], self.data[i]
          self.swaps.append([i, minIndex])
          self.siftDown(minIndex)
          
  def generateSwaps(self):
    for i in range(n // 2, -1, -1):
        self.siftDown(i)
        
  def solve(self):
    self.readData()
    self.generateSwaps()
    self.writeResponse()


if __name__ == '__main__':
    heap_builder = heapBuilder()
    heap_builder.solve()
