import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    
    grid = []
    starts = defaultdict(list)
    max_v = 0
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(N):
            e = row[j]
            if e >= max_v:
                max_v = e
                starts[e].append((i, j))
    
    ans = 0
    for si, sj in starts[max_v]:
        def search(i, j, e, depth=0, chance=True, visited=None):
            if visited is None:
                visited = set()
            visited.add((i, j))
            
            max_depth = 0
            for di, dj in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
                ni, nj = i + di, j + dj
                if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                    continue
                if (ni, nj) in visited:
                    continue
                ne = grid[ni][nj]
                if ne >= e:
                    if chance:
                        ne -= K
                        if ne < e:
                            max_depth = max(max_depth, search(ni, nj, ne, depth + 1, False, visited))
                            visited.remove((ni,nj))
                else:
                    max_depth = max(max_depth, search(ni, nj, ne, depth + 1, chance, visited))
                    visited.remove((ni,nj))
                
            return max_depth + 1
        
        ans = max(ans, search(si, sj, max_v, 0))
    
    print(f"#{t} {ans}")
            
                
            