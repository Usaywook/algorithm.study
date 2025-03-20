import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop, heapify

T = int(input())
for t in range(1, T+1):
    it = iter(map(int, input().split()))
    N = next(it)
    matrix = [list(x) for x in zip(*[it]*N)]

    def getClosenessCentrality(i):
        dist = [N-1] * N
        dist[i] = 0
        queue = [(0, i)]
        visited = [False] * N
        while queue:
            du, u = heappop(queue)
            visited[u] = True
            for v, e in enumerate(matrix[u]):
                if e == 0:
                    continue
                if not visited[v] and du + e < dist[v]:
                    dist[v] = du + e
                    heappush(queue, (dist[v], v))
        return sum(dist)

    ans = (N-1) * N
    for i in range(N):
        ans = min(ans, getClosenessCentrality(i))

    print(f"#{t} {ans}")

