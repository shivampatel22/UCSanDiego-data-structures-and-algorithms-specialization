def majority(A, n):
    if n == 1:
        return 1
    i = 0
    j = i + 1
    num_elem = 0
    count = 0
    while j < n:
        
        while (A[i] == A[j]):
            
            j += 1
            if j == n:
                break
        count = j - i
        if count > n // 2:
            num_elem += 1
        if j < n:
            i = j
            j += 1
    return num_elem
    

if __name__ == '__main__':
    n = int(input())
    A = [int(A) for A in input().split()]
    A.sort()
    print(majority(A, n))