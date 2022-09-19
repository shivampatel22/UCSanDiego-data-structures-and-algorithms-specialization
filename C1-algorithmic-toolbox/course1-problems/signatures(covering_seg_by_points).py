#def my_sort(points):
#    for i in range(1, (2*n)-2, 2):
#        min_index = i
#        min_val = points[min_index]
#        for j in range(i+2, 2*n, 2):
#            if points[j] < min_val:
#                min_index = j
#                min_val = points[min_index]
#        points[min_index], points[i] = points[i], points[min_index] 
#        points[min_index-1], points[i-1] = points[i-1], points[min_index-1]
        #print(min_index)
        #print(min_val)

def maxCommonPts(points):
    points.sort(key = lambda x : x[1])
    #print(points)
    cordinates = []
    i = 0
    while i < n:
        seg = points[i][1]
        cordinates.append(seg)
        p = i+1
        if p >= n:
            #i = p
            break
        arrived = points[p][0]
        while seg >= arrived:
            p += 1
            if p >= n:
                break
            arrived = points[p][0]
        i = p
    print(len(cordinates))
    
    for point in cordinates:
       print(point, end = " ")
            
if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        p1, p2 = map(int, input().split())
        tu = (p1, p2)
        points.append(tu)   
    maxCommonPts(points)
        