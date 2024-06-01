# #Given an array of length n, the longest decreasing subsequence (LDS)
# problem seeks to find a sequence in which the elements of the subsequence
# are listed in the largest to smallest order and the subsequence is as long
# as possible. Give a dynamic programming solution for finding the LDS of
# any given array.
import random as rn

def lds(arr: list[int]) -> list[int]:
    vals = [1 for num in arr]
    prev = [-1 for num in arr]
    for i in range(1, len(arr)):
        candidates = [(vals[j], j) for j in range(i) if arr[j] > arr[i]]
        max_val = max(candidates, key = lambda x:x[0], default = (0,-1))
        vals[i] += max_val[0]
        prev[i] = max_val[1]
        
    lds_index = max(enumerate(vals), key = lambda x:x[1])[0]
    lds_sequence = []
    while(lds_index != -1):
        lds_sequence.append(arr[lds_index])
        lds_index = prev[lds_index]
    return lds_sequence[::-1]

if __name__ == "__main__":
    arr = [rn.randint(0,10) for _ in range(15)]
    print(arr)
    print(lds(arr))
    
    