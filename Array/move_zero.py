def solve(nums):
    """
    utilize swap
    """
    i = 0
    for j in range(len(nums)):        
        if nums[j] != 0:
            print(f"swap nums[{i}] and nums[{j}]")
            nums[i], nums[j] = nums[j], nums[i]
            i += 1                
    return nums        

# nums = [0,1,0,3,12]
# nums = [1,3,0,0,12]
nums = [2,1]
print(solve(nums))