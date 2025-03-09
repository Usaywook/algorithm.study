import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M  = map(int, input().split())

    house = []
    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(N):
            if row[j] == 1:
                house.append((i, j))
    
    def getOperateCost(k):
        return k**2 + (k-1)**2
    
    def getDistance(x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)
    
    def search(i, j, size):
        Q = deque([(i, j, 0)])
        visited = [[0]*N for _ in range(N)]
        visited[i][j] = True 
        c = 0
        while Q:
            i, j, k = Q.popleft()
            if k == size:
                continue
            if grid[i][j] == 1:
                c += 1
                                
            for di, dj in zip((-1,1,0,0),(0,0,-1,1)):
                ni, nj = i + di, j + dj
                if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                    continue
                if not visited[ni][nj]:
                    visited[ni][nj] = True     
                    Q.append((ni, nj, k+1))
        return c
                
    ans = 0
    max_count = len(house)
    for ci in range(N):
        for cj in range(N):
            # max_ck-1 = N 이므로 N+2
            for ck in range(1, N+2):
                operate_cost = getOperateCost(ck)
                count = 0
                if max_count * M - operate_cost < 0:
                    continue

                # count = search(ci, cj, ck)         
                for hi, hj in house:                     
                    if getDistance(hi, hj, ci, cj) <= ck - 1:
                        count += 1         
                if count * M - operate_cost < 0:
                    continue                
                ans =  max(ans, count)
                    
    print(f"#{t} {ans}")
    