def subset_sum(nums: list[int], target: int) -> list[int]:
    nums.sort()
    subset = []
    def helper(index: int = 0):
        if(index == len(nums)): return
        if(sum(subset) + nums[index] <= target):
            subset.append(nums[index])
            helper(index + 1)
            if(sum(subset) == target): return
            subset.pop()
        else:
            return
        helper(index + 1)
        
        
        
        
            
        
    
    
    
    