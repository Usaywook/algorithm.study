import sys
sys.stdin = open("input.txt", "r")

def is_attach(si, sj, size):
    if si + size > 10 or sj + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if grid[si + i][sj + j] == 0:
                return False
    return True

def attach(si, sj, size, value):
    for i in range(size):
        for j in range(size):
            ni, nj = si + i, sj + j
            grid[ni][nj] = value

T = int(input())
for t in range(1, T+1):
    grid = []
    for _ in range(10):
        grid.append(list(map(int, input().split())))
    ones = [(i, j) for i in range(10) for j in range(10) if grid[i][j] == 1]

    counter = {i+1: 5 for i in range(5)}
    def search(depth=0, used_cnt=0):
        global ans
        if used_cnt >= ans:
            return

        if depth == len(ones):
            ans = min(ans, used_cnt)
            return

        i, j = ones[depth]
        if grid[i][j] == 0:
            search(depth+1, used_cnt)
            return

        for k in range(5, 0, -1):
            if counter[k] <= 0:
                continue
            if is_attach(i, j, k):
                attach(i, j, k, 0)
                counter[k] -= 1
                search(depth + 1, used_cnt + 1)
                attach(i, j, k, 1)
                counter[k] += 1

    ans = 25
    search()
    ans = -1 if ans == 25 else ans
    print(f"#{t} {ans}")