def mergeSort(arr):
    if len(arr) < 2:
        return arr
    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]
    print('-----recursion depth + 1-----')
    print('left={}'.format(left))
    print('right={}'.format(right))
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)
    
def merge(L, R):
    print("merging {} and {}".format(L, R))
    A = [None] * (len(L) + len(R))
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return A
    
print(mergeSort([38, 27, 43, 3, 9, 82]))
