import random as rn

def subset_sum(nums: list[int], target: int) -> list[int]:
    nums.sort()
    subset = []
    def helper(index: int = 0):
        if(index == len(nums)): return
        if(sum(subset) + nums[index] <= target):
            print(subset)
            subset.append(nums[index])
            helper(index + 1)
            if(sum(subset) == target): return
            subset.pop()
        else:
            return 
        helper(index + 1)
    helper()
    return subset

n = 15
L = [rn.randint(3*n,4*n) for _ in range(n)] * 3
rn.shuffle(L) 
print(L)
r = rn.randint(n*10, n*15)
print(r)
print(subset_sum(L,r))
        
    
    
    
    