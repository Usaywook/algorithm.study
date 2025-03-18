import sys

sys.stdin = open("input.txt", "r")

from collections import defaultdict, deque

T = int(input())
for t in range(1, T+1):
    N = int(input())

    G = defaultdict(list)
    P = [-1] * (N + 1)
    for i, x in enumerate(map(int, input().split())):
        G[x].append(i + 2)
        P[i+2] = x

    # if t != 3:
    #     continue

    path = []
    def bfs(s):
        Q = deque([(s, 0)])
        visited = set()
        while Q:
            u, d = Q.popleft()
            visited.add(u)
            path.append((u, d))

            for v in G[u]:
                if v not in visited:
                    Q.append((v, d+1))


    # print(G)
    # print(P)
    bfs(1)
    # print(path)

    # bi-direct
    # 복사안하면 반복문 도중 에러 방생가능성 있음.
    graph = defaultdict(list)
    for p, cs in G.items():
        graph[p].extend(cs)
        for c in cs:
            graph[c].append(p)

    def search(s, e):
        Q = deque([(s, 0)])
        visited = set()
        while Q:
            u, d = Q.popleft()
            if u == e:
                return d
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    Q.append((v, d + 1))
        return -1  # 도달할 수 없는 경우

    ans = 0
    for (u, a), (v, b) in zip(path[:-1], path[1:]):
        dist = search(u, v)
        # print(u, v, dist)
        ans += dist
        # if v in G[u]:
        #     ans += 1
        # else:
        #     ans += a + b
    print(f"#{t} {ans}")