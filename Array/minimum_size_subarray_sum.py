def solve(target, nums):
    start = 0    
    # max 보다 크게하는 것에 주의
    ans_length = 10**5 + 1 
    sub_array_sum = 0 
    for end in range(len(nums)):        
        sub_array_sum += nums[end]                                              
        while sub_array_sum >= target:                   
            ans_length = min(end - start + 1, ans_length)    
            sub_array_sum -= nums[start]
            start += 1                        
        
    return 0 if ans_length == 10**5 + 1 else ans_length

target = 7
nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
target = 15
nums = [5,1,3,5,10,7,4,9,2,8]
# print(nums)
print(solve(target, nums))