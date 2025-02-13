def spread():
    visited.clear()
    for e in virus:
        dfs(e[0], e[1])

def dfs(start_x, start_y):        
    visited.add((start_x, start_y))    
    for next_x, next_y in getNeighbors(start_x, start_y):
        e = (next_x, next_y)        
        if next_x < 0 or next_x > N - 1 or next_y < 0 or next_y > M - 1:
            continue        
        if array[next_x][next_y] != 0:
            continue        
        if e in visited:
            continue                
        dfs(next_x, next_y)         

def getNeighbors(x, y):    
    for i in range(4):        
        yield (x + dx[i], y + dy[i])
    
def printArray():    
    print('[', end='')
    for i in range(N):        
        if i == 0:
            print('[', end='')
        else:
            print(' [', end='')
        
        for j in range(M):
            print(array[i][j], end=' ')
        
        if i == N-1:
            print(']', end='')        
        else:            
            print(']')
    print(']')

# array = [[2,0,0,0,1,1,0],
#          [0,0,1,0,1,2,0],
#          [0,1,1,0,1,0,0],
#          [0,1,0,0,0,0,0],
#          [0,0,0,0,0,1,1],
#          [0,1,0,0,0,0,0],
#          [0,1,0,0,0,0,0]]
N, M = list(map(int, input().split()))
array = []
for i in range(N):
    array.append(list(map(int, input().split())))
    
N = len(array)
M = len(array[0])
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited=set()

# printArray()

wall = []
virus = []
empty = []
for i in range(N):
    for j in range(M):
        e = array[i][j]        
        if e == 0:
            empty.append((i,j))
        elif e == 2:                    
            virus.append((i,j))
            

ans = 0
for i in range(len(empty)):
    for j in range(i):
        for k in range(j):
            # 1. make 3 wall in empty space            
            array[empty[i][0]][empty[i][1]] = 1
            array[empty[j][0]][empty[j][1]] = 1
            array[empty[k][0]][empty[k][1]] = 1
            # 2. spread virus
            spread()
            
            # 3. count empty : orinal_empty - selected_wall(3) - virus visited - num_virus
            # count = 0
            # for i in range(N):
            #     for j in range(M):
            #         if array[i][j] == 0 and (i,j) not in visited: 
            #             count += 1
            count = len(empty) - 3 - (len(visited) - len(virus))            
                        
            ans = max(ans, count)     
                   
            # print(ans, count, visited)
            # printArray()
            
            array[empty[i][0]][empty[i][1]] = 0
            array[empty[j][0]][empty[j][1]] = 0
            array[empty[k][0]][empty[k][1]] = 0
            
print(ans)