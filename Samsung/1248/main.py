import sys
sys.stdin = open("input.txt", "r")

from collections import defaultdict, deque

T = int(input())
for t in range(1, T+1):
    V, E, p, q = map(int, input().split())

    graph = defaultdict(list)
    parent = [-1] * (V + 1)
    for u, v in zip(*[iter(map(int, input().split()))]*2):
        graph[u].append(v)
        parent[v] = u

    def find_path(node):
        path = []
        while node != -1:
            path.append(node)
            node = parent[node]
        return path[::-1]

    def find_lca(u, v):
        lca = -1
        for a, b in zip(find_path(u), find_path(v)):
            if a == b:
                lca = a
            else:
                break
        return lca

    def bfs(s):
        queue = deque([s])
        visited = set()
        cnt = 0
        while queue:
            u = queue.popleft()
            visited.add(u)
            cnt += 1
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
        return cnt

    r = find_lca(p, q)
    ans = bfs(r)
    print(f"#{t} {r} {ans}")