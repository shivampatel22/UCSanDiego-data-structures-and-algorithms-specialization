def binaryFindPos(arr, elem, high, low):
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