def solve1(data):
    def solveRecursive(n, m, cache={}):
        if (n,m) in cache:
            return cache[(n,m)]
        if n < 0:
            return False
        if m == 0:
            return True
        elif m < 0:
            return False
        
        ans = solveRecursive(n-1, m - data[n-1]) or solveRecursive(n-1, m)        
        cache[(n,m)] = ans
        return ans
    
    subset_sum = sum(data)
    if subset_sum % 2 != 0:    
        return False
    else:
        return solveRecursive(len(data), int(subset_sum // 2))

def solve2(data):
    def solveIterative(n, m):
        # initilize
        memo = [[False]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            memo[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                memo[i][j] = memo[i-1][j]                                        
                k = j-data[i-1]
                if k >= 0:                                
                    memo[i][j] = memo[i][j] or memo[i-1][k]        
            
        return memo[n][m]

    subset_sum = sum(data)    
    if subset_sum % 2 != 0:        
        return False
    return solveIterative(len(data), int(subset_sum // 2))
    
# data = [2,1,2,3,4]
# data = [1,5,11,5]
# data = [1,2,3,5]
data = [1,2,5]
# print(solve1(data))
print(solve2(data))

