
def count_inversions(arr: list[int]) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]: count += 1
    return count


    
L = [8, 2, 3, 1]

print(count_inversions(L))
    

    
  