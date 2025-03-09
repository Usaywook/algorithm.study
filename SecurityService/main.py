import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M  = map(int, input().split())

    grid = []
    for i in range(N):
        grid.append(list(map(int, input().split())))
    
    def getOperateCost(k):
        return k**2 + (k-1)**2
    
    di = (-1,1,0,0)
    dj = (0,0,-1,1)
    def search(i, j, size, depth=0):
        global count, ci, cj
        if abs(ci-i) + abs(cj-j) >= size:
            return
        if grid[i][j] == 1:
            count += 1
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                continue
            if not visited[ni][nj]:
                search(ni, nj, size, depth+1)
    
    ans = 0
    for ci in range(N):
        for cj in range(N):
            max_dist = max([abs(ci-u) + abs(cj-v)+1 for u in range(N) for v in range(N)])
            for ck in range(1, max_dist+1):
                operate_cost = getOperateCost(ck)
                
                count = 0
                visited = [[0]*N for _ in range(N)]                
                search(ci, cj, ck)
                cost = count * M - operate_cost
                if cost < 0:
                    continue
                    
                if count > ans:
                    ans = count 
                    
    print(f"#{t} {ans}")
    