def solve(nums1, m, nums2, n):
    i,j,k = m-1, n-1, m+n-1
    while j >= 0 and i >= 0:                
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]            
            i -= 1
        else:            
            nums1[k] = nums2[j]
            j -= 1
        k -= 1        
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1  
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1         
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1 = [1]
m = 1
nums2 = []
n = 0
nums1 = [0]
m = 0
nums2 = [1]
n = 1
nums1 = [2,0]
m = 1
num2 = [1]
n = 1
print(solve(nums1, m, nums2, n))