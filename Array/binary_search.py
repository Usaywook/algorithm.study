def RecursiveBS(arr, low, high, x):
    if high < low:
        return -1
    else:
        mid = low + (high - low) // 2
        if arr[mid] ==  x:
            return mid
        elif arr[mid] > x:
            return RecursiveBS(arr, low, mid-1, x)  
        else:
            return RecursiveBS(arr, mid+1, high, x)

def IterativeBS(arr, low, high, x):
    while low <= high:
        mid  = low + (high - low) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
        

arr = [2, 3, 4, 10, 40]
x = 10

result = ResursiveBS(arr, 0, len(arr)-1, x)
print(result)
result = IterativeBS(arr, 0, len(arr)-1, x)
print(result)