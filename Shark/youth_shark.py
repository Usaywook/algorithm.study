def printMaze(maze):
    assert len(maze) == 4 and len(maze[0]) == 4
    for i in range(4):
        print("\t", maze[i])
    print()


class Solver:
    def __init__(self):        
        self.di = [-1,  -1, 0, 1    , 1, 1, 0, -1]
        self.dj = [0, -1, -1, -1, 0, 1, 1, 1]
        
    def solve(self, maze):        
        # init shark, fish, maze
        shark = [0, 0, *maze[0][0]] # i, j, num, move        
        
        fishes = []
        for i in range(4):
            for j in range(4):               
                fish = [i, j, maze[i][j][0], maze[i][j][1]]
                if i == shark[0] and j == shark[1]:
                    fish[-1] = -1                
                fishes.append(fish)                
        fishes.sort(key=lambda x: x[2])    
                                    
        return self.dfs(shark, fishes, maze)
        
                                
    def dfs(self, shark, fishes, maze, depth=0):
        # movefishes                         
        for fish in fishes:  
            i, j, num, move = fish
            # isAlive
            if move == -1:
                continue
            for k in range(8):
                next_move = (move + k - 1) % 8
                next_i = i + self.di[next_move]
                next_j = j + self.dj[next_move]
                # outBound
                if next_i < 0 or next_i > 3 or next_j < 0 or next_j > 3:
                    continue
                # isShark
                if next_i == shark[0] and next_j == shark[1]:                    
                    continue
                
                # swap fish
                next_num = maze[next_i][next_j][0]
                if next_num != 0:                                    
                    fishes[next_num-1][0], fishes[next_num-1][1] = i, j                    
                fish[0], fish[1], fish[3] = next_i, next_j, next_move + 1
                maze[next_i][next_j], maze[i][j] = (num, next_move + 1), maze[next_i][next_j] 
                break
        
        # moveShark             
        ans = 0   
        for k in range(1, 4):            
            i, j, num, move = shark            
            next_i = i + k * self.di[move-1]
            next_j = j + k * self.dj[move-1]            
            # outBound
            if next_i < 0 or next_i > 3 or next_j < 0 or next_j > 3:
                continue
            # isEmpty
            fish = maze[next_i][next_j]            
            if fish[1] == -1:
                continue                                
            
            # eat fish    
            shark[0], shark[1] = next_i, next_j
            shark[2] = num + fish[0]
            shark[3] = fish[1]            
            maze[i][j] = (0, -1)
            maze[next_i][next_j] = (shark[2], shark[3])            
            fishes[fish[0]-1][3] = -1                        
            
            # call dfs            
            ans = max(ans, self.dfs(shark, [fish[:] for fish in fishes], [row[:] for row in maze], depth+1))            
            
            # rollback shark & maze & fishes to before eat fish
            shark = [i, j, num, move]                        
            maze[i][j] = (num, move)
            maze[next_i][next_j] = (fish[0], fish[1])
            fishes[fish[0]-1][3] = fish[1]
        
        return shark[2] if ans==0 else ans
        
        
import sys
sys.stdin = open('youth_shark.txt', 'r')
T = int(input())
for t in range(T):    
    maze = []
    for _ in range(4):
        line = list(map(int, input().split()))        
        maze.append(list(zip(line[::2], line[1::2])))    
        
    ans = Solver().solve(maze)
    print(ans)        
    # break