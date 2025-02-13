from collections import deque
di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]

def solve():
    # print_maze()
    max_dist = -1000
    # safe_pos = None
    
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1: continue                
            dist = getDistance(i, j)
            if dist > max_dist:
                max_dist = dist
                # safe_pos = (i, j)
    
    print(max_dist)
    # print(f"safe pos = {safe_pos}, max_dist = {max_dist}")
    

def getDistance(start_i, start_j):
    visited = [[False] * M for _ in range(N)]
    visited[start_i][start_j] = True
    queue = deque()
    queue.append((start_i, start_j, 0))
    min_dist = 1000
    target = None
    while queue:
        pos_i, pos_j, dist = queue.popleft()
        
        # maze[pos_i][pos_j] = 2
        # print_maze()
        
        if dist >= min_dist: continue
        
        for k in range(8):
            next_i = pos_i + di[k]
            next_j = pos_j + dj[k]
            if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > M - 1: continue 
            if visited[next_i][next_j]: continue
            visited[next_i][next_j] = True
            
            next_dist = dist + 1
            if maze[next_i][next_j] == 1:
                min_dist = next_dist
                target = (next_i, next_j)
                
            queue.append((next_i, next_j, next_dist))
    
    return min_dist

def print_maze():
    for i in range(N):
        print(maze[i])
    print()
        
import sys
sys.stdin = open("baby_shark2.txt", 'r')
T = int(input())
for t in range(T):
    # print(f"#{t}")
    N, M = list(map(int, input().split()))
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input().split())))
    solve()