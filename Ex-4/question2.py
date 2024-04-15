
def count_inversions(arr: list[int]) -> int:

    def merge(arr: list[int], left: list[int], right: list[int]) -> int:
        i = 0
        j = 0
        k = 0
        inversions = 0
        left_len = len(left)
        right_len = len(right)
        while i < left_len and j < right_len:

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            
            else:
                arr[k] = right[j]
                j += 1
                inversions += left_len - i

            k += 1
        
        
        while i < left_len:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < right_len:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return inversions


    n = len(arr)
    if n <= 1:
        return 0
    
    left = arr[:n//2]
    right = arr[n//2:]
    count_left = count_inversions(left)
    count_right = count_inversions(right)
    count = merge(arr, left, right) + count_left + count_right
    return count

    
L = [8, 2, 3, 1]

print(count_inversions(L))
    

    
  