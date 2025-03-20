from heapq import heappush, heappop, heapify

edges = [
    ('a', 'b', 29),
    ('a', 'f', 10),
    ('b', 'g', 15),
    ('b', 'c', 16),
    ('c', 'd', 12),
    ('d', 'g', 18),
    ('d', 'e', 22),
    ('e', 'g', 25),
    ('e', 'f', 27)
]

def kruskal():
    def makeset():
        for v in V:
            P[v] = v
            R[v] = 0

    def find(x):
        if P[x] == x:
            return x
        else:
            P[x] = find(P[x])
            return P[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if R[x] < R[y]:
            P[x] = y
        else:
            P[y] = x
            if R[x] == R[y]:
                R[x] += 1

    P = {}
    R = {}
    makeset()
    
    cost = 0
    # 간선의 비용 순으로 정렬
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        # u 와 v가 서로소 이면 합침
        if find(u) != find(v):
            union(u, v)
            cost += w
            print(f"{u} - {w} - {v}")
    return cost

from collections import defaultdict
def primRecursive(s, tree=[], cost=0, visited=None):
    if len(tree) == len(V) - 1:
        return cost
    
    if visited is None:
        visited = {v:False for v in V}
    visited[s] = True
    
    min_e = None
    min_w = 1000
    for e, w in graph[s]:
        if visited[e]:
            continue
        if w < min_w:            
            min_e = e
            min_w = w
    if min_e is not None:
        print(f"{s} - {min_w} - {min_e}")
        return primRecursive(min_e, tree + [(s, min_e)], cost + min_w, visited)

def primIterative(start):
    """
    graph: 각 노드에 대해 (이웃 노드, 가중치) 튜플의 리스트를 가지는 딕셔너리
    start: 시작 노드
    """
    visited = set()  # MST에 포함된 노드들을 저장
    min_heap = []  # (가중치, 시작노드, 도착노드)를 저장하는 최소 힙
    total_cost = 0  # MST의 총 비용

    # 시작 노드를 방문하고, 시작 노드와 인접한 모든 간선을 최소 힙에 추가
    visited.add(start)
    for neighbor, w in graph[start]:
        heappush(min_heap, (w, start, neighbor))

    while min_heap:
        weight, frm, to = heappop(min_heap)
        # 이미 방문한 노드면 스킵
        if to in visited:
            continue

        # 새로운 노드를 방문하고, 간선의 가중치를 비용에 추가
        visited.add(to)
        total_cost += weight
        print(f"{frm} - {weight} - {to}")

        # 새로 방문한 노드의 인접 간선들을 최소 힙에 추가
        for neighbor, w in graph[to]:
            if neighbor not in visited:
                heappush(min_heap, (w, to, neighbor))

    return total_cost


def prim_simple(start):
    """
    간선정보 저장할 필요없나면 간단하게 이와같이 구현
    """
    visited = set()
    min_heap = []
    total_cost = 0

    visited.add(start)
    for neighbor, weight in graph[start]:
        heappush(min_heap, (weight, neighbor))

    while min_heap:
        weight, node = heappop(min_heap)
        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heappush(min_heap, (w, neighbor))

    return total_cost

graph = defaultdict(list)
V = set()
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))
    V.add(u)
    V.add(v)
    
print(kruskal())
print(primRecursive('a'))
print(primIterative('a'))
print(prim_simple('a'))