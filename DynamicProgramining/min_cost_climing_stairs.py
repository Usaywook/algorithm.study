def solveRecursive(n):
    """ 
    f[n] = min(f[n-1] + cost[n-1], f[n-2] + cost[n-2])
    base case : f[0] = 0, f[1] = 0, 
    ex) : f[2] = min(c[0], c[1]), f[3]  = min(f[2] + c[2, f[1] + c[1]), ... 
    f[n] is minimum cost to reach (n+1)-th stair with jump 1 or 2 steps
    """
    if n < 2:
        return 0
    return min(solveRecursive(n-1) + cost[n-1], solveRecursive(n-2) + cost[n-2])

def solveIterative(n):
    ans = [0] * (n+1)
    for i in range(2, n+1):
        ans[i] = min(ans[i-1] + cost[i-1], ans[i-2] + cost[i-2])
    return ans[n]

if __name__ == '__main__':
    global cost 
    cost =  [1,2,4,6,2,4,6,1]
    
    ans = solveRecursive(len(cost))
    print(ans)
    ans = solveIterative(len(cost))
    print(ans)