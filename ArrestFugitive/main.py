import sys
sys.stdin = open("input.txt", "r")

from collections import deque

di, dj = (0, -1, 1, 0, 0), (0, 0, 0, - 1, 1)
graph = {
    0: [],
    1: [1, 2, 3, 4],
    2: [1, 2],
    3: [3, 4],
    4: [1, 4],
    5: [2, 4],
    6: [2, 3],
    7: [1, 3],
}
in_dir = {dir: k for k, dir in enumerate(zip(di, dj))}

T = int(input())
for t in range(1, T+1):    
    N, M, R, C, L = map(int, input().split())

    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    
    def search(i, j):                   
        visited = [[False] * M for _ in range(N)]            
        count = 0        
    
        Q = deque([(i, j, 0)])  
        visited[i][j] = True
        while Q:
            i, j, depth =  Q.popleft()     
                                                     
            if depth >= L:    
                continue
                                
            count += 1 
                                                                                                
            for k in graph[grid[i][j]]:                
                ni, nj = i + di[k], j + dj[k]
                                
                if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
                    continue
                
                ne = grid[ni][nj]
                                
                if ne == 0:
                    continue
                
                if in_dir[(-di[k], -dj[k])] not in graph[ne]:                    
                    continue
                
                if not visited[ni][nj]:          
                    visited[ni][nj] = True
                    Q.append((ni, nj, depth + 1))                       
         
        return count           
                           
    count = search(R, C)            
    print(f"#{t} {count}")    
