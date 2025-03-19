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

    path = []
    ans = 0
    def bfs(s):
        """
        tree라서 간선수는 n - 1
        연산시간은 O(n)
        """
        Q = deque([(s, 0)])
        visited = set()
        while Q:
            u, d = Q.popleft()
            visited.add(u)
            path.append((u, d))

            for v in G[u]:
                if v not in visited:
                    Q.append((v, d+1))

    bfs(1)

    def findLowestCommonAncestor(u, v, cnt = 0):
        """
        최악의 경우 O(N)
        """
        while u != v:
            u, v = P[u], P[v]
            cnt += 2
        return cnt

    # 최종적으로 연산시간은 O(N^2)
    for (u, a), (v, b) in zip(path[:-1], path[1:]):
        if a == b:
            ans += findLowestCommonAncestor(u, v, 0)
        elif a + 1 == b:
            ans += findLowestCommonAncestor(u, P[v], 1)
        else:
            raise NotImplementedError

    print(f"#{t} {ans}")