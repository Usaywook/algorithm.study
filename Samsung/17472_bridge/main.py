#9 10 9 -1
import sys
sys.stdin = open("input.txt", "r")

from collections import deque, defaultdict
import heapq

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        grid.append(list(map(int, input().split())))

    ground = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                ground[(i, j)] = len(ground)

    def is_out(i, j):
        if i < 0 or i > N - 1 or j < 0 or j > M - 1:
            return True
        return False

    def bfs(si, sj, sk, ind):
        global visited
        visited[sk] = 1
        grid[si][sj] = ind
        queue = deque([(si, sj, 0)])

        while queue:
            i, j, d = queue.popleft()
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
                queue.append((ni, nj, d+1))

    # 섬 분할
    visited = [0] * len(ground)
    num_nodes = 0
    for (i, j), k in ground.items():
        if visited[k]:
            continue
        bfs(i, j, k, num_nodes + 2)
        num_nodes += 1

    # 다리 후보 찾기
    # bridges = []
    graph = defaultdict(dict)
    for i, j in ground.keys():
        start = grid[i][j]
        for di, dj in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            length = 0
            ni, nj = i + di, j + dj
            while not is_out(ni, nj):
                end = grid[ni][nj]
                if end == start:
                    break
                if end > 0:
                    if length > 1:
                        # bridges.append((start, end, length))
                        graph[start][end] = min(graph[start].get(end, 10), length)
                    break
                ni += di
                nj += dj
                length += 1

    # 최소 신장 트리 구하기
    visited = [0] * num_nodes
    min_heap = []
    # parent = {}
    ans = 0
    start = 2
    visited[start-2] = 1
    for neighbor, w in graph[start].items():
        heapq.heappush(min_heap, (w, start, neighbor))

    while min_heap:
        w, frm, to = heapq.heappop(min_heap)

        if visited[to-2]:
            continue
        visited[to-2] = 1
        ans += w
        # parent[to] = frm

        for neighbor, w in graph[to].items():
            if not visited[neighbor-2]:
                heapq.heappush(min_heap, (w, to, neighbor))

    # print(parent)
    ans = -1 if sum(visited) != num_nodes else ans # 모든 섬을 연결할 수 없는 경우 -1
    print(f"#{t} {ans}")


