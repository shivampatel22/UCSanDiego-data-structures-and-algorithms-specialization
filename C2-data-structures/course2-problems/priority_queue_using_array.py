"""naive priority queue implementation using arrays.extractMax() runs in O(n)."""
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def printQueue(self):
        print("queue = {}".format(self.queue))
        print("size = {}".format(self.size))
        return
    
    def insert(self, key):
        self.queue.append(key)
        self.size += 1
        print("inserted {} in the queue".format(key))
        return
    
    def extractMax(self):
        if self.isEmpty():
            print("queue is empty")
            return
        m = self.queue[0]
        max_index = 0 
        for index, value in enumerate(self.queue):
            if self.queue[index] > m:
                m = self.queue[index]
                max_index = index
        self.queue.pop(max_index)
        self.size -= 1
        print("maximum = {}".format(m))
        return
    
    def remove(self, it):
        try:
            self.queue.remove(it)
        except ValueError:
            print("{} is not in the queue".format(it))
        else:
            self.size -= 1
            print("removed {} from the queue".format(it))
        return
        
    def getMax(self):
        print("max = {}".format(max(self.queue)))
        return
    
    def changePriority(self, it, p):
        flag = 0 
        for index, value in enumerate(self.queue):
            if value == it:
                flag = 1 
                self.queue[index] = p
        if flag == 0:
            print ("element not found in queue")
        else:
            print("changed priority of {} to {}".format(it, p))
    
if __name__ == '__main__':
    p_queue = PriorityQueue()
    #p_queue.extractMax()
    p_queue.insert(10)
    p_queue.insert(5)
    p_queue.insert(11)
    p_queue.insert(20)
    p_queue.insert(0)   
    #p_queue.extractMax()
    p_queue.remove(100)
    p_queue.getMax()
    p_queue.changePriority(20, 1)
    p_queue.printQueue()
    
        