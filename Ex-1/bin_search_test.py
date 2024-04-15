def binary_search_iterative(arr: list[int], key: int) -> int:
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        check_val = arr[mid]
        if (key < check_val): right = mid - 1
        elif (key > check_val): left = mid + 1
        else: return mid
    
    return -1

def binary_search_recursive(arr: list[int], key: int) -> int:
    if(len(arr) == 0):
        return -1
    
    if(len(arr) == 1 and arr[0] == key):
        return 0
    
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    check_val = arr[mid]
    if (key < check_val): return binary_search_recursive(arr[:mid])
    if (key > check_val): return binary_search_recursive(arr[mid+1:])
    return mid

