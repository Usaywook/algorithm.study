#9 10 9 -1
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        grid.append(list(map(int, input().split())))

    ground = {}
    nonground = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                ground[(i, j)] = len(ground)
            else:
                nonground.append((i, j))

    parent = []
    rank = []
    for (i, j), k in ground.items():
        parent.append(k)
        rank.append(0)

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    def is_out(i, j):
        if i < 0 or i > N - 1 or j < 0 or j > M - 1:
            return True
        return False

    def bfs(si, sj, sk, ind):
        global visited
        visited[sk] = 1
        grid[si][sj] = ind
        queue = deque([(si, sj, sk, 0)])

        while queue:
            i, j, k, d = queue.popleft()
            for di, dj in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
                ni, nj = i + di, j + dj
                if is_out(ni, nj):
                    continue
                if grid[ni][nj] == 0:
                    continue
                nk = ground[(ni, nj)]
                if visited[nk]:
                    continue
                visited[nk] = 1
                grid[ni][nj] = ind
                union(k, nk)
                queue.append((ni, nj, nk, d+1))

    visited = [0] * len(ground)
    num_nodes = 0
    for (i, j), k in ground.items():
        if visited[k]:
            continue
        bfs(i, j, k, num_nodes + 1)
        num_nodes += 1

    ans = MAX = N * M * (num_nodes - 1)
    def search(d = 0, res=0, nodes=set()):
        global ans
        if d == len(nonground):
            return

        if len(nodes) == num_nodes:
            # print(f"leaf: {ans}, {res}, {nodes}")
            ans = min(ans, res)
            return

        if res > ans:
            return ans

        i, j = nonground[d]
        # print(i, j, d)

        for di, dj in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            ni, nj = i + di, j + dj
            if is_out(ni, nj):
                continue
            if grid[ni][nj] == 0:
                continue
            begin = grid[ni][nj]

            def search_ground(si, sj, di, dj, length=0):
                ni, nj = si + di, sj + dj

                if is_out(ni, nj):
                    return 0
                if grid[ni][nj] == 0:
                    return search_ground(ni, nj, di, dj, length + 1)
                else:
                    return 0 if grid[ni][nj] in nodes else length + 1

            length = search_ground(i, j, -di, -dj)
            if length <= 1:
                continue
            ei, ej = i - length * di, j - length * dj
            end = grid[ei][ej]
            # print(f"{d} / {len(nonground)}: {(ni, nj)}, {(ei, ej)}, {begin}-{length}-{end}, {res + length}")
            search(d+1, res + length, nodes | {begin, end})

        search(d+1, res)

    if t != 1:
        continue

    # for g in grid:
    #     print(g)
    # print()

    search()
    ans = -1 if ans == MAX else ans
    print(f"#{t} {ans}")


