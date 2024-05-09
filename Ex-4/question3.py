prev_pivot = 0 
def lcs(arr: list[int]) -> int:
    def largest_contiguous_sum(arr: list[int]):
        if len(arr) == 0: return float('-inf')
        if len(arr) == 1: return arr[0]
        pivot = None
        s = 0
        for i in range(len(arr)):
            if arr[i] < 0:
                pivot = i
                break
            s += arr[i]
        if pivot is None: return s
        s_left = sum(arr[:pivot])
        s_right = largest_contiguous_sum(arr[pivot + 1:])
        global prev_pivot
        max_val = max(s_left, s_right, s_left + sum(arr[pivot:prev_pivot]))
        prev_pivot = pivot
        return max_val
    return largest_contiguous_sum(arr)
L = [1,2,3,-4,5,-8]
print(lcs(L))