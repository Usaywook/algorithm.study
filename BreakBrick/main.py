import sys
sys.stdin = open("input.txt", "r")

def print_bricks(bricks):
    for row in bricks:
        print(row)
    print()        

def dfs(j, depth, bricks):
    # find start point
    def find_start(j):
        i = 0
        e = 0
        for k in range(H):
            if bricks[k][j] != 0:
                i = k
                e = bricks[i][j]
                break
        return i, e

    # remove bricks with chain reaction        
    def remove(si, sj, se):
        bricks[si][sj] = 0    
        for k in range(1, se):
            for di, dj in directions:
                ni, nj = si + k * di, sj + k * dj
                if ni < 0 or ni > H-1 or nj < 0 or nj > W-1:
                    continue
                if bricks[ni][nj] == 0:
                    continue                                            
                remove(ni, nj, bricks[ni][nj])

    def move():
        for k in range(W):
            p = H-1    
            for q in range(H-1,-1,-1):
                if bricks[q][k] != 0:
                    bricks[p][k], bricks[q][k] = bricks[q][k], bricks[p][k]
                    p -= 1    
                    
    def count():
        cnt = 0
        for i in range(H):
            for j in range(W):
                if bricks[i][j] != 0:
                    cnt += 1
        return cnt    
    
    global ans
    if depth == N:       
        ans = min(ans, count())
        return 
    i, e = find_start(j)
    remove(i, j, e)
    move()
    for k in range(W):
        dfs(k, depth+1, [row[:] for row in bricks])
        
T = int(input())
for t in range(T):
    global N, W, H, directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    ans = W*H
    for k in range(W):        
        dfs(k, 0, [row[:] for row in bricks])
    
    print(f"#{t+1} {ans}")