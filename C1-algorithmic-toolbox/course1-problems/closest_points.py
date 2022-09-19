import math
import sys
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return(math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))

def bruteForce(P,n):
    minDist = sys.maxsize
    for i in range(n):
        for j in range(i+1,n):
            minDist = min(minDist, distance(P[i], P[j]))
    return minDist

def minStripDist(strip, size, d):
    minDist = d
    strip.sort(key = lambda point: point.y)
    for i in range(size):
        j = i+1
        while j<size and (strip[j].y - strip[i].y < minDist):
            minDist = distance(strip[i], strip[j])
            j += 1
    return minDist
    
def findClosest(P, n):
    if n <= 3:
        return bruteForce(P,n)
    mid = n//2
    midPoint = P[mid]
    left_min = findClosest(P[:mid], mid)
    right_min = findClosest(P[mid:], n-mid)
    d = min(left_min, right_min)
    
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
            
    return(min(d, minStripDist(strip, len(strip), d)))

def closest(P, n): 
    P.sort(key = lambda point: point.x) 
    return findClosest(P, n) 

P = [Point(2, 3), Point(12, 30), 
     Point(40, 50), Point(5, 1),  
     Point(12, 10), Point(3, 4)] 
n = len(P)  
print("The smallest distance is",  closest(P, n))