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
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            cost += w
            print(f"{u} - {w} - {v}")
    return cost

from collections import defaultdict
def prim(s, tree=[], cost=0, visited=None):    
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
        return prim(min_e, tree + [(s, min_e)], cost + min_w, visited)

graph = defaultdict(list)
V = set()
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))
    V.add(u)
    V.add(v)
    
print(kruskal())
print(prim('a'))