def solve(nums):
    p, q, r = 0, 0, len(nums) - 1
    
    while q <= r:        
        if nums[q] == 0:            
            nums[p], nums[q] = nums[q], nums[p]            
            # print(f'swap nums[{p}] and nums[{q}]', nums)
            p += 1                    
            q += 1                 
        elif nums[q] == 2:            
            nums[r], nums[q] = nums[q], nums[r]
            # print(f'swap nums[{r}] and nums[{q}]', nums)
            r -= 1                 
        else:
            q += 1
    return nums
        
# nums = [2,0,2,1,1,1]
# nums = [2,0,1]
nums = [1,2,0]
# print(solve(nums))
from itertools import permutations
for perm in permutations(range(len(nums))):
    check = [nums[p] for p in perm]
    # print(check)
    print("ans: ", solve(check))   
    break