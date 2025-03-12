import sys
sys.stdin = open("input.txt", "r")

di, dj = (-1, 1, 1, -1), (1, 1, -1, -1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    def search(i, j, si, sj, visited, checked, d=0, direction=0, length=-1):
                                 
        for k in range(direction, max(direction + 1, 4)):
            ni, nj = i + di[k], j + dj[k]
            
            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                continue              
            
            if d > 1 and (ni == si and nj == sj):                
                length = max(length, d + 1)  
                # print(f"visit ({si}, {sj}), depth = {d + 1}, checked = {checked}")    
                # for v in visited:
                #     print(v)
                # print()
                return length
            
            ne = grid[ni][nj]
            if ne in checked:
                continue
            
            if not visited[ni][nj]:      
                visited[ni][nj] = 1
                checked.add(grid[ni][nj])          
                tmp = search(ni, nj, si, sj, visited, checked, d + 1, k, length)
                length = max(length, tmp)  
                visited[ni][nj] = 0
                checked.remove(ne)                
        
        return length

    ans = -1
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]     
            visited[i][j] = 1     
            checked = set([grid[i][j]])                   
            cnt = search(i, j, i, j, visited, checked)            
            ans = max(ans, cnt)
            
    print(f"#{t} {ans}")

    