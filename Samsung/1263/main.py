import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict
from heapq import heappush, heappop, heapify

T = int(input())
for t in range(1, T+1):
    it = iter(map(int, input().split()))
    N = next(it)
    # matrix = [list(x) for x in zip(*[it]*N)]
    graph = defaultdict(list)
    for i in range(N):
        for j in range(N):
            e = next(it)
            if e != 0:
                graph[i].append(j)

    def getClosenessCentrality(i):
        dist = [N-1] * N
        dist[i] = 0
        queue = [(0, i)]
        visited = [False] * N
        while queue:
            du, u = heappop(queue)
            visited[u] = True
            for v in graph[u]:
                if not visited[v] and du + 1 < dist[v]:
                    dist[v] = du + 1
                    heappush(queue, (dist[v], v))
        return sum(dist)

    ans = (N-1) * N
    for i in range(N):
        ans = min(ans, getClosenessCentrality(i))

    print(f"#{t} {ans}")

