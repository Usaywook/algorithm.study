import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1
    for r in range(N):
        for c in range(2, N):
            if grid[r][c]:
               continue
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
            if grid[r][c-1] or grid[r-1][c]:
                continue
            dp[r][c][2] = sum(dp[r-1][c-1])

    ans = sum(dp[N-1][N-1])
    print(f"#{t} {ans}")
