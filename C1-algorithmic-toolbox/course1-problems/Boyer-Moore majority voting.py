def majorityElement(arr, right):
    """returns 1 is a majority element exists and -1 is it doesn't."""
    maxIndex = 0
    count = 1
    for i in range(1, right):
        if arr[i] == arr[maxIndex]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maxIndex = i
            count = 1
    
    count = 0    
    for i in range(right):
        if arr[i] == arr[maxIndex]:
            count += 1
    if count > len(arr)//2:
        return 1
    else:
        return -1
        
print(majorityElement([1, 2, 3, 4], 4))