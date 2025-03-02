import sys
sys.stdin = open("input.txt", "r")

def print_cells(states):
    grid = [0,0,0,0]
    for key, value in states.items():
        for i, j, s, c in value:
            grid[0] = min(grid[0], i)
            grid[1] = max(grid[1], i)
            grid[2] = min(grid[2], j)
            grid[3] = max(grid[3], j)

    cells = [[0 for j in range(grid[3] - grid[2] + 1)] for i in range(grid[1] - grid[0] + 1)]
    
    for key, value in states.items():
        for x, y, s, c in value:
            prefix = "\033[33m" if s == 0 else "\033[34m"
            cells[x - grid[0]][y - grid[2]] = prefix + str(key) + "\033[0m"    
            
    for row in cells:
        for col in row:
            print(col, end=" ")
        print()    

            
from collections import OrderedDict

T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
        
    pos_table = set()
    
    # 초기 상태
    def initialize():
        states = OrderedDict()
        for i in range(N):
            row = list(map(int, input().split()))
            for j in range(M):
                e = row[j]
                if e == 0:
                    continue
                if e in states.keys():
                    states[e].append((i, j, 0, 0))                
                else:
                    states[e] = [(i, j, 0, 0)]    
                pos_table.add((i, j))            
        states = OrderedDict(sorted(states.items(), key=lambda x: x[0], reverse=True))
        return states    
    
    # 번식
    def reproduce(states):
        new_states = OrderedDict()
        for x in states.keys():
            new_states[x] = []
        for x, cells in states.items():
            for i, j, s, c in cells:            
                c += 1            
                if s == 0:
                    if c >= x:
                        s = 1    
                    new_states[x].append((i, j, s, c))
                    continue                        
                                
                if c < 2 * x:
                    new_states[x].append((i, j, s, c))                
                
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if (ni, nj) not in pos_table:
                        new_states[x].append((ni, nj, 0, 0))
                        pos_table.add((ni, nj))
        return new_states
    
    # 번식 세포 계산
    def count_cells(states):
        count = 0
        for key, values in states.items():
            count += len(values)
        return count
    
    cur_states = initialize()    
    # print_cells(cur_states)
    # print()
    
    for k in range(K):        
        cur_states = reproduce(cur_states)                
        count = count_cells(cur_states)
        
        # print(f"{k} step")
        # print_cells(cur_states)
        # print(count)
        # print() 

    print(f"#{test_case} {count}")                       