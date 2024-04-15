import random as rn

def kth_smallest_insertion(arr: list[int], k: int) -> int:
    for i in range(len(arr)):
        key = arr[i]
        j = i
        while(j > 0 and arr[j-1] > key):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
        print(arr)
    return arr[k-1]

def kth_smallest_quick(arr: list[int], k: int) -> int:
    print(arr)
    print("k", k)
    if(arr == []): return -1
    pivot_index = rn.randrange(0, len(arr))
    pivot = arr[pivot_index]
    print("Pivot :", pivot)
    greater_index = len(arr) - 1
    for i in range(greater_index, -1 , -1):
        if(arr[i] > pivot):
            arr[i], arr[greater_index] = arr[greater_index], arr[i]
            if(pivot_index == greater_index): pivot_index = i
            greater_index -= 1
            print("Greater index:", greater_index)
    arr[greater_index], arr[pivot_index] = arr[pivot_index], arr[greater_index]
    if greater_index == k - 1: return arr[greater_index]
    if greater_index < k - 1: return kth_smallest_quick(arr[greater_index + 1:], (k - greater_index - 1))
    return kth_smallest_quick(arr[:greater_index], k)


arr = [1,6,9,2,4,3,7,8,5]
print(kth_smallest_quick(arr, 7))