import sys
from collections import deque
from collections import OrderedDict
sys.stdin = open("adult_shark.txt")

di = (-1,1,0,0)
dj = (0,0,-1,1)

N,M,K = list(map(int, input().split()))
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

current_direction = list(map(int, input().split()))
priorities = []
for _ in range(M):    
    priority = []
    for _ in range(4):
        priority.append(list(map(int, input().split())))
    priorities.append(priority)

def printMaze(maze):
    for i in range(N):
        print(maze[i])
    print()
    
def printShark(sharkes):
    for key, value in sharkes.items():
        print(key, value)
    print()
    
def solve():
    # initialize shark
    # shark state = {num: pos, }
    # cell state = num, scent
    maze = []
    sharkes = {}
    for i in range(N):
        row = []
        for j in range(N):
            if data[i][j] > 0:
                shark_num = data[i][j]
                sharkes[shark_num] = deque([(i, j)], maxlen=K)
                row.append([shark_num, K])
            else:
                row.append([0, 0])
        maze.append(row)
        
    # dont consider remove shark when sort with acending order
    # sharkes = OrderedDict(sorted(sharkes.items(), key=lambda x: x[0], reverse=True))
    sharkes = OrderedDict(sorted(sharkes.items(), key=lambda x: x[0]))
    printMaze(maze)
    print(f"direction: {current_direction}")
    printShark(sharkes)
    
    return dfs(sharkes, maze, M)

def dfs(sharkes, maze, shark_count, step=0):
    # utill 1000 step
    if step == 1000:
        return -1
    # if 1 shark remain return step
    if shark_count == 1:
        return step
    
    # for debug
    # if step == ${debug}:
    #     return step
    # print(f"Step {step+1}")
    # print()
    
    # find next pos 
    for shark_num, traj in sharkes.items():
        # is out shark -> skip
        if current_direction[shark_num-1] == -1:
            continue
        
        # generate candidates
        cand = []
        pos_i, pos_j = traj[-1]
        for k in range(4):
            next_pos_i = pos_i + di[k]
            next_pos_j = pos_j + dj[k]
            # out of Bound
            if next_pos_i < 0 or next_pos_i > N-1 or next_pos_j < 0 or next_pos_j > N-1:
                continue
            next_shark_num, next_shark_shadow = maze[next_pos_i][next_pos_j]
            # shadow
            if next_shark_shadow != 0:
                continue
            cand.append(k+1)
            
        
        if len(cand) == 0:
            for k in range(4):
                next_pos_i = pos_i + di[k]
                next_pos_j = pos_j + dj[k]
                # out of Bound
                if next_pos_i < 0 or next_pos_i > N-1 or next_pos_j < 0 or next_pos_j > N-1:
                    continue
                next_shark_num, _ = maze[next_pos_i][next_pos_j]
                # shadow
                if shark_num != next_shark_num:
                    continue
                cand.append(k+1)
                    
        # consider priority          
        priority = priorities[shark_num-1][current_direction[shark_num-1]-1]                    
        temp = []
        for direction in cand:
            for idx, prior in enumerate(priority):
                if direction == prior:
                    temp.append((direction, idx))
        temp.sort(key=lambda x: x[1])
        direction = temp[0][0]
        
        # set direction
        current_direction[shark_num-1] = direction                
        
    # update shark & map
    for shark_num, traj in sharkes.items():
        # for K = 1, traj has been empty 
        if len(traj) == 0:
            continue
        prev_pos_i, prev_pos_j = traj[-1]
        
        # update shadow   
        seen = set()     
        for k in range(len(traj)):
            pos_i, pos_j = traj[len(traj) - 1 - k]
            if maze[pos_i][pos_j][1] > 0 and (pos_i, pos_j) not in seen:
                maze[pos_i][pos_j][1] -= 1
                seen.add((pos_i, pos_j))
            if maze[pos_i][pos_j][1] == 0:
                maze[pos_i][pos_j][0] = 0
                traj.popleft()
                
        # is alive
        if current_direction[shark_num-1] == -1:
            continue
        
        # update trajectory
        direction = current_direction[shark_num-1]
        curr_pos_i = prev_pos_i + di[direction-1]
        curr_pos_j = prev_pos_j + dj[direction-1]       
                
                
        # is_out_shark -> set direction = -1       
        next_shark_num, _ = maze[curr_pos_i][curr_pos_j]        
        if  next_shark_num !=0 and next_shark_num < shark_num:
            current_direction[shark_num-1] = -1
            shark_count -= 1
            continue
        
        # move shark 
        maze[curr_pos_i][curr_pos_j] = [shark_num, K]
        traj.append((curr_pos_i, curr_pos_j)) 
        
        
    printMaze(maze)
    print(f"shark_count: {shark_count}")
    print(f"direction: {current_direction}")
    printShark(sharkes)
    
    
    # recursive call
    step = dfs(sharkes, maze, shark_count, step+1)
    
    # rollback        
    return step
    
print(solve())
    