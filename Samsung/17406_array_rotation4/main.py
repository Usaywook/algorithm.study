import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,M,K = map(int, input().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))
rotates = []
for _ in range(K):
    rotates.append(list(map(int, input().split())))

def rotate_matrix(arr, order):
    for ind in order:
        r,c,s = rotates[ind]
        for k in range(1, s + 1):
            top, bottom = r - k - 1, r + k - 1
            left, right = c - k - 1, c + k - 1

            # 가장자리 값을 시계 방향으로 한 칸씩 회전
            prev = arr[top][left]

            # 위쪽 행 (왼쪽에서 오른쪽)
            for j in range(left + 1, right + 1):
                arr[top][j], prev = prev, arr[top][j]

            # 오른쪽 열 (위에서 아래로)
            for i in range(top + 1, bottom + 1):
                arr[i][right], prev = prev, arr[i][right]

            # 아래쪽 행 (오른쪽에서 왼쪽)
            for j in range(right - 1, left - 1, -1):
                arr[bottom][j], prev = prev, arr[bottom][j]

            # 왼쪽 열 (아래에서 위로)
            for i in range(bottom - 1, top - 1, -1):
                arr[i][left], prev = prev, arr[i][left]

    res = 100 * 50
    for a in arr:
        res = min(res, sum(a))
    return res

select = []
visited = [0] * K
ans = 100 * 50
def search(depth):
    global ans
    if depth == K:
        ans = min(ans, rotate_matrix([a[:] for a in array], select))
        return
    for i in range(K):
        if visited[i]:
            continue
        visited[i] = 1
        select.append(i)
        search(depth+1)
        select.pop()
        visited[i] = 0

search(0)
print(ans)


