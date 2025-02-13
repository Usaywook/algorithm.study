def solve(data):    
    memo = [0] * len(data)
    memo[0] = data[0]
    ans = -10**4
    for i in range(1, len(data)):
        memo[i] = max(memo[i-1] + data[i], data[i])
        ans = max(ans, memo[i])
    return ans

def solveOpt(data):        
    ans = tmp = data[0]            
    for i in range(1, len(data)):
        tmp = max(tmp + data[i], data[i])
        ans = max(ans, tmp)
    return ans

data = [-2,1,-3,4,-1,2,1,-5,4]
print(solve(data))
print(solveOpt(data))