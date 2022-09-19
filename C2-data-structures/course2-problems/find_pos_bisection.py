def binaryFindPos(arr, elem, high, low):
    """this function returns the position/index(0 based), where the given element should be 
    inserted in the given array using bisection algorithm."""
    while high >= low:
        
        mid = (high + low) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1
    if low > mid:
        return mid + 1
    else:
        return mid

if __name__ == '__main__':
    print(binaryFindPos([1,2,5,6], 3, 3, 0))