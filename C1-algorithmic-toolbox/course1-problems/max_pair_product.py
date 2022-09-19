def max_pairwise_prod(a, l):
    maximum = a[0]
    max_index = 0
    for i in range(l):
        if a[i] > maximum:
            maximum = a[i]
            max_index = i
            
    second_maximum = 0
    for i in range(l):
        if a[i] > second_maximum and i != max_index:
            second_maximum = a[i]
            
    p = maximum * second_maximum
    return p
    
if __name__ == '__main__':
    l = int(input())
    a = [int(x) for x in input().split()]
    print(max_pairwise_prod(a, l))
       
        