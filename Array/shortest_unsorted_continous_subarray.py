def solve(nums):
    N = len(nums)
    if N < 2: return 0
    MAX = 10**5
    min_peak, max_peak = MAX + 1, -MAX - 1
    min_peak_idx, max_peak_idx = -1, N
    start, end = 1, 0
    for i in range(N-1):
        if nums[i] > nums[i+1] and nums[i+1] < min_peak:
            min_peak = nums[i+1]
            min_peak_idx = i+1
    for i in range(min_peak_idx, -1, -1):                
        if nums[i] > min_peak:        
            start = i        
    for i in range(N-1, 0, -1):        
        if nums[i] < nums[i-1] and nums[i-1] > max_peak:
            max_peak = nums[i-1]
            max_peak_idx = i-1                
    for i in range(max_peak_idx, N):        
        if nums[i] < max_peak:                    
            end = i        
    print(min_peak, max_peak)
    print(min_peak_idx, max_peak_idx)
    print(start, end)    
    print(nums[start:end+1])    
    return end - start + 1

nums = [2,6,4,8,10,9,15]
nums = [1,2,3,4]
# nums = [1]
# nums = [5,4,3,2,1]
# nums = [1,3,2,2,2]
# nums = [1,1,3,2,2]
# nums = [2,3,3,2,4]
# nums = [1,3,2]
print(solve(nums))