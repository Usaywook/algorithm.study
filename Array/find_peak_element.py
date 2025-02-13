def solve(nums):
    i, j = 0, len(nums) - 1
    k = (i + j) // 2
    # print(i, k, j)
    while i < j:        
        if nums[k] < nums[k+1]:
            i = k + 1            
        else:
            j = k
        k = (i + j) // 2    
        # print(i, k, j)        
    return j

nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
print(solve(nums))