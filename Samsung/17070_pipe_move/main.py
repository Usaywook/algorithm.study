import sys

sys.stdin = open("input.txt", "r")

dr, dc = (0,1,1), (1,0,1)
# 이동
move = {
    0: [0, 2], # 가로
    1: [1, 2], # 세로
    2: [0, 1, 2], # 대각선
}
# 벽 체크
check = {
    0: [0], # 가로
    1: [1], # 세로
    2: [0,1,2], # 대각선
}

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    def is_out(r, c):
        if r < 0 or r > N-1 or c < 0 or c > N-1:
            return True
        return False

    def search(sr, sc, s_dir=0):
        if sr == N-1 and sc == N-1:
            return 1
        if (sr, sc, s_dir) in memo:
            return memo[(sr, sc, s_dir)]

        cnt = 0
        for n_dir in move[s_dir]:
            is_hazard = False
            for c_dir in check[n_dir]:
                cr, cc = sr + dr[c_dir], sc + dc[c_dir]
                if is_out(cr, cc) or grid[cr][cc]:
                    is_hazard = True
                    break
            if is_hazard:
                continue
            nr, nc = sr + dr[n_dir], sc + dc[n_dir]
            if is_out(nr, nc):
                continue
            cnt += search(nr, nc, n_dir)

        memo[(sr, sc, s_dir)] = cnt
        return cnt

    memo = {}
    ans = search(0, 1, 0)
    print(f"#{t} {ans}")