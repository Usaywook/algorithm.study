import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    it = iter(map(int, input().split()))
    N = next(it)

    matrix = [[(N-1) * N] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            e = next(it)
            if i == j:
                matrix[i][j] = 0
            if e == 1:
                matrix[i][j] = 1

    # using FloydWarshall
    # Time Complexity : O(N^3)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    ans = (N-1) * N
    for i in range(N):
        ans = min(ans, sum(matrix[i]))

    print(f"#{t} {ans}")



