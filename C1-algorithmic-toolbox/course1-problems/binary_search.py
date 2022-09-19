def binary_search(A, k, high, low):
    while low <= high:
        mid = (high + low) // 2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            high = mid - 1
        elif A[mid] < k:
            low = mid + 1
            
    return -1
            
if __name__ == '__main__':
    n1A = [int(n1A) for n1A in input().split()]
    n1 = n1A[0]
    A = n1A[1:]
    n2K = [int(n2K) for n2K in input().split()]
    K = n2K[1:]
    for k in K:
        print(binary_search(A, k, n1-1, 0), end = ' ')