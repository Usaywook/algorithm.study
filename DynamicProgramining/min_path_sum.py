def solveRecursitve(i, j):
    if i == 0 and j == 0:
        return cost[0][0]
    if i == 0:
        return solveRecursitve(0, j-1) + cost[0][j]
    if j == 0:
        return solveRecursitve(i-1, 0) + cost[i][0]
     
    return min(solveRecursitve(i-1, j), solveRecursitve(i, j-1)) + cost[i][j]

        
def solveIterative():
    M = len(cost)
    N = len(cost[0])
    # Base
    ans = [[0]*M for _ in range(N)]
    ans[0][0] = cost[0][0]
    for i in range(1, N):
        ans[i][0] = ans[i-1][0] + cost[i][0]
    for j in range(1, M):
        ans[0][j] = ans[0][j-1] + cost[0][j]

    # Process
    for i in range(1, N):
        for j in range(1, M):
            ans[i][j] = min(ans[i-1][j], ans[i][j-1]) + cost[i][j]
                
    return ans[N-1][M-1]


if __name__ == '__main__':
    global cost
    cost = [[1,3,1,2],[2,4,5,2],[3,4,5,6],[1,5,6,2]]
    print(solveRecursitve(3,3))
    print(solveIterative())