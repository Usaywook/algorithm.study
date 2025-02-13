import sys
sys.stdin = open("./input.txt", "r")

def parse_array():
    array = []
    N = int(input())
    for i in range(N):
        array.append(list(map(int, input().split())))
    return array, N

def print_array(array, prefix=''):
    for i in range(len(array)):
        print(prefix + ' '.join(map(str, array[i])))

def is_end(N, array, curr_x, curr_y, visited, cnt, min_ans):
    if cnt > min_ans:
        return True
    elif curr_x < 0 or curr_x > N - 1 or curr_y < 0 or curr_y > N - 1:
        return True
    elif visited[curr_x][curr_y]:
        return True
    elif array[curr_x][curr_y] == 0:
        return True
    elif curr_x + curr_y + cnt > min_ans: 
        # curr_x + curr_y 는 남은 최단거리
        return True

def backTracking(array, prev_x, prev_y, curr_x, curr_y, visited=None, cnt=0, min_ans=float("inf")):
    """
    (1) 현재 진입 타일, 진입 방향 뿐만 아니라 파이프 이용 이력을 State에 반영한다.
    (2) 정방향과 역방향을 모두 고려한다. <- 이 문제에서 갈림길은 끽해야 2개이기 때문에 아마 이것으로도 충분할거라고 생각합니다.
    """
    # initialize
    N = len(array)
    if visited is None:
        visited = [[False for _ in range(N)] for _ in range(N)]
    
    if curr_x == 0 and curr_y == -1:
        if cnt < min_ans:
            min_ans = cnt
        return min_ans
    
    # end condition
    if is_end(N, array, curr_x, curr_y, visited, cnt, min_ans):
        return min_ans
        
    # backtracking by current state
    visited[curr_x][curr_y] = True
    
    if array[curr_x][curr_y] < 3:
        # line pipe can not change direction
        if curr_x == prev_x:
            # from horizental -> to horizental (change y)
            next_x = curr_x 
            next_y = curr_y + curr_y - prev_y
        else:
            # from vertical -> to vertical
            next_x = curr_x + curr_x - prev_x
            next_y = curr_y 
        min_ans = backTracking(array, curr_x, curr_y, next_x, next_y, visited, cnt+1, min_ans)
        
    else:
        # bent pipe can change direction
        if curr_x == prev_x:
            # from horizental -> to up & down
            min_ans = backTracking(array, curr_x, curr_y, curr_x-1, curr_y, visited, cnt+1, min_ans)
            min_ans = backTracking(array, curr_x, curr_y, curr_x+1, curr_y, visited, cnt+1, min_ans)
        else:
            # from vertical -> to left & right            
            min_ans = backTracking(array, curr_x, curr_y, curr_x, curr_y-1, visited, cnt+1, min_ans)
            min_ans = backTracking(array, curr_x, curr_y, curr_x, curr_y+1, visited, cnt+1, min_ans)
                    
    visited[curr_x][curr_y] = False
    
    return min_ans

T = int(input())
for test_case in range(1, T + 1):
    array, N = parse_array()
    print(f'#{test_case}', end=" ")    
    
    final_min = backTracking(array, N - 1, N, N - 1, N - 1)
    print(final_min)