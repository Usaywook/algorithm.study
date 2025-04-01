import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_score = 0
order = [0] * 9
used = [False] * 9
used[0] = True  # 1번 선수 고정 (index 0), 이미 사용된 것으로 처리


def simulate(order):
    score, p = 0, 0
    for inning in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            result = arr[inning][order[p]]
            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif result == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif result == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            elif result == 4:
                score += b3 + b2 + b1 + 1
                b3, b2, b1 = 0, 0, 0
            p = (p + 1) % 9
    return score

# DFS로 타순을 만드는 함수 (index를 사용하여 최적화)
def dfs(idx):
    global max_score

    if idx == 9:
        res = simulate(order)
        if res > max_score:
            max_score = res
        return

    if idx == 3:  # 4번 타자 고정
        order[idx] = 0
        dfs(idx + 1)
        return

    for i in range(1, 9):
        if not used[i]:
            used[i] = True
            order[idx] = i
            dfs(idx + 1)
            used[i] = False

dfs(0)
print(max_score)