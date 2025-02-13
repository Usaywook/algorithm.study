def solve(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        right_sum -= nums[i]
        print(f"sum{nums[:i]}) ={left_sum}, sum({nums[i+1:]}) = {right_sum}")
        if right_sum == left_sum:
            return i
        left_sum += nums[i]
                
    return -1
    

nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
print(solve(nums))
