import sys


def parse_array():
    array = []
    N = int(input())
    for i in range(N):
        array.append(list(map(int, input().split())))
    return array, N

def print_array(array, prefix=''):
    for i in range(len(array)):
        print(prefix + ' '.join(map(str, array[i])))

def backtracking(prev_x, prev_y, idx_x, idx_y, cnt):
    """
    Perform a backtracking search to find the minimum cost path in a grid with specific pipe rules.

    Args:
        prev_x (int): The previous x-coordinate.
        prev_y (int): The previous y-coordinate.
        idx_x (int): The current x-coordinate.
        idx_y (int): The current y-coordinate.
        cnt (int): The current cost (number of moves).

    Returns:
        None: Updates the global variable `final_min` to store the minimum cost.
    """
    global final_min, N, input_map, visit

    if cnt > final_min:
        return
    elif idx_x == 0 and idx_y == -1:
        if cnt < final_min:
            final_min = cnt
        return
    elif idx_x < 0 or idx_x >= N or idx_y < 0 or idx_y >= N:
        return
    elif visit[idx_x][idx_y]:
        return
    elif input_map[idx_x][idx_y] == 0:
        return
    elif idx_x + idx_y + cnt > final_min:
        return

    visit[idx_x][idx_y] = True

    if input_map[idx_x][idx_y] < 3:
        # line pipe
        if prev_x == idx_x:
            # case 1
            next_x = idx_x
            next_y = idx_y + (idx_y - prev_y)
        else:
            # case 2
            next_x = idx_x + (idx_x - prev_x)
            next_y = idx_y
        backtracking(idx_x, idx_y, next_x, next_y, cnt + 1)

        # backtracking(idx_x, idx_y, next_x, next_y, cnt + 1)

    else:
        # bent pipe
        if prev_x == idx_x:
            # up or down
            backtracking(idx_x, idx_y, idx_x - 1, idx_y, cnt + 1)
            backtracking(idx_x, idx_y, idx_x + 1, idx_y, cnt + 1)
        else:
            # left or right
            backtracking(idx_x, idx_y, idx_x, idx_y - 1, cnt + 1)
            backtracking(idx_x, idx_y, idx_x, idx_y + 1, cnt + 1)

    visit[idx_x][idx_y] = False


sys.stdin = open("./input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    array, N = parse_array()
    prefix = '\t' 
    print(f'test_case: {test_case}, N = {N}')    
    # print_array(array, prefix)
    
    visit = [[False] * N for _ in range(N)]
    input_map = array
    final_min = 3000
    backtracking(N - 1, N, N - 1, N - 1, 0)
    print(prefix + f'ans = {final_min}')
    # ///////////////////////////////////////////////////////////////////////////////////
