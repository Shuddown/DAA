def lcs(arr: list[int]) -> int:
    if(len(arr) == 0): return -1
    if(len(arr) == 1): return arr[0]
    mid = len(arr)//2
    max_left = lcs(arr[mid:])
    max_right = lcs(arr[:mid])
    max_mid = arr[0]
    sum_t = 0
    for num in arr:
        sum_t += num
        max_mid = max(max_mid, sum_t)
        sum_t = max(sum_t, 0)
    return max(max_left, max_right, max_mid)


    
    
L = [-1,-2,-3,4,5,-6,-7,-8]
print(lcs(L))