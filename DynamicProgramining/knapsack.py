def solveRecursive(n, w):
    # base
    if n == 0 or w <= 0:
        return 0
    if w-weight[n-1] < 0:
        return solveRecursive(n-1, w)
    return max(solveRecursive(n-1, w-weight[n-1]) + value[n-1], solveRecursive(n-1, w))  
    
def solveIterative(n, w):
    ans = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            v = value[i-1]
            q = j - weight[i-1]
            
            c1 = 0 if q < 0 else ans[i-1][q] + v
            c2 = ans[i-1][j]
            
            ans[i][j] = max(c1, c2)
    return ans[n][w] 

if __name__ == "__main__":
    global value, weight
    value = [30,20,40,10]
    weight = [1,2,3,4]
    ans = solveRecursive(4, 1)
    print(ans)
    ans = solveIterative(4, 1)
    print(ans)
    ans = solveRecursive(4, 5)
    print(ans)
    ans = solveIterative(4, 5)
    print(ans)