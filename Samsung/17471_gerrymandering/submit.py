import sys
input = sys.stdin.readline


N = int(input())
people = list(map(int, input().split()))
num_edges = []
graph = {}
for i in range(N):
    line = list(map(int, input().split()))
    num_edges.append(line[0])
    graph[i] = line[1:]

nodes = list(range(N))
features = [0] * N
MAX = 100 * 10 + 1
ans = MAX
def search(depth):
    global ans
    if depth == N:
        if sum(features) == 0 or sum(features) == N:
            return

        s0, s1 = -1, -1
        for i in range(N):
            if features[i] == 0:
                s0 = i
                break
        for i in range(N):
            if features[i] == 1:
                s1 = i
                break
        visited = [0] * N
        def dfs(start, num=0):
            feature = features[start]
            num += people[start]
            visited[start] = 1
            stack = [(start, 0)]
            while stack:
                u, d = stack.pop()
                if d == N:
                    continue
                for neighbor in graph[u]:
                    v = neighbor - 1
                    if features[v] != feature:
                        continue
                    if visited[v]:
                        continue
                    num += people[v]
                    visited[v] = 1
                    stack.append((v, d+1))
            return num

        p0 = dfs(s0)
        p1 = dfs(s1)
        if sum(visited) == N:
            ans = min(ans, abs(p0 - p1))
        return

    search(depth + 1)
    features[depth] = 1
    search(depth + 1)
    features[depth] = 0

search(0)
ans = -1 if ans == MAX else ans
print(ans)


