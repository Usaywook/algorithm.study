import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    # make sets
    parent = {}
    diff = {}
    rank = {}
    for i in range(N):
        parent[i+1] = i+1
        diff[i+1] = 0
        rank[i+1] = 0

    def find(x):
        p = parent[x]
        if p != x:
            # 재귀 호출 시 만나는 모든 부모노드를 root의 child로 만들고 반환
            parent[x] = find(p)
            # 재귀 호출 시 만나는 모든 부모노드의 무게차이로 대표노드와의 무게차이 갱신
            diff[x] += diff[p]
        return parent[x]

    def union(a, b, w):
        """
        시간 복잡도는 o(h)
        """
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
            diff[ra] = - w - diff[a] + diff[b]
        else:
            parent[rb] = ra
            diff[rb] = w + diff[a]  - diff[b]
            if rank[ra] == rank[rb]:
                rank[ra] += 1

    ans = []
    # 최종적인 시간복잡도는 최악의 경우 O(MN)
    for _ in range(M):
        it = iter(input().split())
        query = next(it)
        if query == "!":
            a, b, w = map(int, map(next, [it] * 3))
            # print(query, a, b, w)
            union(a, b, w)

        elif query == "?":
            a, b = map(int, map(next, [it] * 2))
            # print(query, a, b)
            if find(a) == find(b):
                ans.append(str(diff[b] - diff[a]))
            else:
                ans.append('UNKNOWN')

    ans = " ".join(ans)
    print(f"#{t} {ans}")