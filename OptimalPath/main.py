import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nodes = [pair for pair in zip(*[iter(map(int, input().split()))] * 2)]

    def getDist(u, v):
        a, b = nodes[u], nodes[v]
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    ans = 200 * N + 1
    visited = [False] * (N + 2)
    visited[0] = True
    memo = {}
    def search(cur_ind, mask, dist):
        global ans
        # 이미 좋은 해보다 거리가 길면 가지치기
        if dist >= ans:
            return

        # 동일 상태에 대해 이미 더 좋은 해를 찾았다면 더 이상 진행하지 않음
        if (cur_ind, mask) in memo and memo[(cur_ind, mask)] <= dist:
            return
        memo[(cur_ind, mask)] = dist

        # 모든 고객(총 N명)을 방문했다면, 집(노드 index 1)까지의 거리 추가 후 최적해 갱신
        if mask == (1 << N) - 1:
            ans = min(ans, dist + getDist(cur_ind,1))
            return

        # 고객 노드는 index 2부터 N+1까지
        for next_ind in range(2, N + 2):
                bit = 1 << (next_ind - 2)
                if mask & bit:  # 이미 방문한 경우 스킵
                    continue
                search(next_ind, mask | bit, dist + getDist(cur_ind,next_ind))

    search(0, 0, 0)
    print(f"#{t} {ans}")


