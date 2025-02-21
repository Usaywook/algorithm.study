import sys
sys.stdin = open('input.txt', 'r')

T = int(input().strip())
block_table = {
    1: {1:2, 2:4, 3:1, 4:3},
    2: {1:4, 2:1, 3:2, 4:3},
    3: {1:3, 2:1, 3:4, 4:2},
    4: {1:2, 2:3, 3:4, 4:1},
    5: {1:2, 2:1, 3:4, 4:3},    
}

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def simulate(x, y, k):      
    stack = [(0, x, y, k, 0)]
    while stack:
        e, i, j, k, cnt = stack.pop()                 
        if e == -1:
            break                    
        ni = i + di[k-1]
        nj = j + dj[k-1]        
        if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
            cnt = 2 * cnt + 1
            break
        if ni == x and nj == y:
            break
        ne = grid[ni][nj]                
        if ne == 0:
            stack.append((ne, ni, nj, k, cnt))
        elif 0 < ne < 6:                        
            stack.append((ne, ni, nj, block_table[ne][k], cnt+1))
        elif 5 < ne < 11:                 
            ni, nj = hole_table[(ni, nj)]       
            stack.append((ne, ni, nj, k, cnt))
        elif ne == -1:
            break        
    return cnt

for t in range(T):
    global grid, hole_table
    grid = []
    hole_table = {}    
    N = int(input().strip())
    for i in range(N):        
        row = list(map(int, input().strip().split()))
        for j in range(N):             
            e = row[j]                 
            if e > 5:
                if e not in hole_table:
                    hole_table[e] = (i, j)
                else:
                    key = hole_table.pop(e)
                    hole_table[(i, j)] = key
                    hole_table[key] = (i, j)        
        grid.append(row)

    max_ans = 0    
    for i in range(N):
        for j in range(N):
            for k in range(1, 5):                    
                if grid[i][j] == 0:     
                    ans = simulate(i, j, k)                                        
                    max_ans = max(max_ans, ans)                        
        
    print(f"#{t+1} {max_ans}")    