from collections import OrderedDict

def printMaze(maze):
    for i in range(N):
        print(maze[i])
    print()
    
def printShark(sharkes):
    for key, value in sharkes.items():
        print(key, value)
    print()
    
def solve(debug=False):
        
    # 초기 격자 초기화 (num, scent)
    # 상어 초기화 {num: [row, col, direction]}
    maze = [[(0, 0) for _ in range(N)] for _ in range(N)]
    sharkes = dict()
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] != 0:
                shark_num = row[j]
                # 방향은 나중에 초기화
                sharkes[shark_num] = [i, j, 0]
                maze[i][j] = (shark_num, K)
            
    # 각 상어의 초기 방향 
    for idx, direction in enumerate(list(map(int, input().split()))):
        sharkes[idx+1][2] = direction
    
    # 번호가 작은 상어부터 이동하기 위한 정렬
    sharkes = OrderedDict(sorted(sharkes.items(), key=lambda x: x[0]))
    
    # 각 상어별 우선순위 방향
    priorities = dict()
    for i in range(1, M+1):    
        priority = dict()
        for j in range(1, 5):
            priority[j] = list(map(int, input().split()))
        priorities[i] = priority
    
    if debug:
        printMaze(maze)
        printShark(sharkes)
    
    # 1000회 반복
    for step in range(1000):        
        # 남은 상어가 1마리면 종료
        if len(sharkes) == 1:
            return step
        
        # 업데이트를 위한 상어 상태 선언
        visited = set()
        new_sharks = OrderedDict()
        
        # 번호가 작은 상어부터 이동 (동시에 이동하되, 충돌 시 번호가 큰 상어는 제거)
        for shark_num, (pos_i, pos_j, direction) in sharkes.items():
            
            # 다음 위치 방향 찾기
            new_pos_i, new_pos_j, new_direction = -1, -1, -1
            
            # 인접한 칸 중 냄새가 없는 칸을 우선순위에 따라 탐색
            moved = False            
            for next_direction in priorities[shark_num][direction]:
                next_pos_i = pos_i + di[next_direction - 1]
                next_pos_j = pos_j + dj[next_direction - 1]
                # 격자 밖 제외
                if next_pos_i < 0 or next_pos_i > N-1 or next_pos_j < 0 or next_pos_j > N-1:
                    continue 
                # 냄새 있다면 제외
                _, smell = maze[next_pos_i][next_pos_j]                
                if smell != 0:
                    continue
                new_pos_i, new_pos_j, new_direction = next_pos_i, next_pos_j, next_direction
                moved = True
                break
                
                
            # 만약 냄새 없는 칸이 없으면 우선순위에 따라 탐색 중 자신의 냄새가 있는 칸으로 이동
            if not moved:
                for next_direction in priorities[shark_num][direction]:
                    next_pos_i = pos_i + di[next_direction - 1]
                    next_pos_j = pos_j + dj[next_direction - 1]
                    # 격자 밖 제외
                    if next_pos_i < 0 or next_pos_i > N-1 or next_pos_j < 0 or next_pos_j > N-1:
                        continue 
                    next_shark_num, _ = maze[next_pos_i][next_pos_j]
                    # 자신의 냄새가 아니면 제외
                    if shark_num != next_shark_num:
                        continue
                    new_pos_i, new_pos_j, new_direction = next_pos_i, next_pos_j, next_direction
                    moved = True
                    break
            
            assert moved
            
            # 업데이트할 상어 정보 저장
            # 충돌 처리: sharks 의 key를 정렬했기 때문에 이미 visited 되었다면 new_sharks 에 정보를 추가하지 않고 넘어감
            if (new_pos_i, new_pos_j) not in visited:
                visited.add((new_pos_i, new_pos_j))
                new_sharks[shark_num] = [new_pos_i, new_pos_j, new_direction]
            
        # 냄새를 업데이트               
        for i in range(N):
            for j in range(N):
                num, smell = maze[i][j]
                if num != 0:
                    smell -= 1
                    if smell == 0:
                        num = 0
                    maze[i][j] = (num, smell)
                    
        # 상어를 업데이트
        for num, (i, j, _) in new_sharks.items():
            maze[i][j] = (num, K)
        
        sharkes = new_sharks
        
        if debug:
            printMaze(maze)
            printShark(sharkes)

    return -1

if __name__ == "__main__":
    import sys
    sys.stdin = open("adult_shark.txt")
    T = int(input())
    global di, dj, N, M, K
    
    for t in range(T):    
        di = (-1,1,0,0)
        dj = (0,0,-1,1)

        N,M,K = list(map(int, input().split()))
        
        ans = solve(False)
        print(ans)