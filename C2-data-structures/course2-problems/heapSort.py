def buildHeap(arr, size):
    


def heapSort(arr, size):
    buildHeap(arr,size)
    s = size-1
    while s>=1:
        arr[0],arr[s] = arr[s],arr[0]
        s -= 1
        shiftDown(0)
        
    