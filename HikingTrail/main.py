import sys
sys.stdin = open("input.txt", "r")
sys.path.append("../")

from collections import defaultdict

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    grid = []
    starts = defaultdict(list)
    max_v = 0
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(N):
            e = row[j]
            if e >= max_v:
                max_v = e
                starts[e].append((i, j))

    ans = 0
    for si, sj in starts[max_v]:
        def search(i, j, e, depth=0, chance=True, visited=None):
            if visited is None:
                visited = set()
            visited.add((i, j))

            max_length = 0
            for di, dj in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
                ni, nj = i + di, j + dj
                if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                    continue
                if (ni, nj) in visited:
                    continue
                ne = grid[ni][nj]
                if ne >= e:
                    if chance:
                        for k in range(1, K+1):
                            if ne - k < e:
                                max_length = max(max_length, search(ni, nj, ne - k, depth + 1,False, visited))
                                visited.remove((ni,nj))
                else:
                    max_length = max(max_length, search(ni, nj, ne, depth + 1, chance, visited))
                    visited.remove((ni,nj))

            return max_length + 1
        ans = max(ans, search(si, sj, max_v, 0))

    print(f"#{t} {ans}")