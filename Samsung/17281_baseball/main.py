import sys
sys.stdin = open("input.txt", "r")

player = list(range(9))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    def simulate(order):
        p = 0
        score = 0
        for inning in range(N):
            out = 0
            base = [0, 0, 0]
            while out < 3:
                k = arr[inning][order[p]]
                if k == 0:
                    out += 1
                elif k == 1:
                    score += base[2]
                    base[2], base[1], base[0] = base[1], base[0], 1
                elif k == 2:
                    score += base[2] + base[1]
                    base[2], base[1], base[0] = base[0], 1, 0
                elif k == 3:
                    score += base[2] + base[1] + base[0]
                    base[2], base[1], base[0] = 1, 0, 0
                elif k == 4:
                    score += base[2] + base[1] + base[0] + 1
                    base = [0] * 3
                else:
                    raise NotImplementedError
                p = (p + 1) % 9
        return score

    def dfs(order=[], used=[False]*len(player)):
        global ans
        if len(order) == len(player):
            res = simulate(order)
            ans = max(ans, res)
            return

        if len(order) == 3:
            order.append(0)
            used[0] = True
            dfs(order, used)
            used[0] = False
            order.pop()
            return

        for i in range(1, len(player)):
            if used[i]:
                continue
            order.append(i)
            used[i] = True
            dfs(order, used)
            used[i] = False
            order.pop()

    ans = 0
    dfs()
    print(f"#{t} {ans}")