import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

import heapq

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def simulate(enemies):
    # O(궁수 수 * 적의 수 * log(적의 수)
    # 성 도달한 적 카운트
    global min_reach
    cnt = 0
    while enemies:
        # 가지치기: 이전에 도달한 적 보다 많아지면 = 제거할 적 적어지면 그만
        if cnt > min_reach:
            return total_e - cnt

        # 궁수의 적 상태 업데이트
        # 굳수 수 * 적 수 * log (범위 안 적 수)
        archers = {p: [], q: [], r: []}
        for k, v in archers.items():
            for er, ec in enemies:
                d = distance(er, ec, N, k)
                if d > D:
                    continue
                else:
                    heapq.heappush(v, (d, ec, er))
        # print(f"archers: {archers}")

        # 적 제거할 적 설정
        targets = set()
        for k, v in archers.items():
            if len(v):
                _, ec, er = heapq.heappop(v)
                targets.add((er, ec))
        # print(f"targets: {targets}")

        # 적 제거 & 이동 & 카운트
        new_enemies = set()
        for er, ec in enemies - targets: # 적 제거
            if er + 1 > N - 1:
                cnt += 1 # 성 도달한 적 카운트
                continue
            new_enemies.add((er + 1, ec))
        enemies = new_enemies
        # print(f"enemies: {enemies}")

    min_reach = min(min_reach, cnt)
    return total_e - cnt # 제거된 적의 수 반환

T = int(input())
for t in range(1, T + 1):
    N, M, D = map(int, input().split())
    enemies = set()
    e_cnt = [0] * M
    # O(MN)
    for i in range(N):
        for j, e in enumerate(list(map(int, input().split()))):
            if e == 1:
                e_cnt[j] += 1
                enemies.add((i, j))
    e_list = sorted(list(range(M)), key=lambda x: e_cnt[x], reverse=True)
    total_e = len(enemies)
    # print(e_list)

    # O(MC3 * sim)
    # sim =  적의 수 * log 적의 수
    ans = 0
    min_reach = total_e
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                p, q, r = e_list[i], e_list[j], e_list[k]
                # print(f"start: {p}, {q}, {r}")
                ans = max(ans, simulate(enemies.copy()))
    print(f"#{t} {ans}")