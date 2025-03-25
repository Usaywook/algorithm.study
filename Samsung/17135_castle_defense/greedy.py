import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def simulate(i, j, k):
    # O(N * 궁수 수(3) * 적 수)
    # 처치한 적 카운트
    global ans, max_ans, found
    cnt = 0
    # 각 행의 적 죽었는지 M 비트 마스크로 체크
    mask = [0] * N
    for turn in range(N):
        # 가지치기: 처치한 적 + 남아 있는 적 < 이전에 처치한 적의 최대값
        # 남아있는 적 = 남은 턴 수 * 궁수 수
        if cnt + (N - turn) * 3 <= ans:
            break
        if cnt + e_cum_cnt[turn] <= ans:
            break

        # 궁수의 타겟 설정
        shoot = set()
        for a_ind in (i, j, k):
            # 거리, 열, 성벽 도달까지 남은 턴
            for d, c, r in e_priority[a_ind]:
                # 놓친 적 제외
                if turn > r:
                    continue
                # 턴별 업데이트 된 위치에서 유효사거리 검사
                if d - turn > D:
                    continue
                # 살아있는지 검사
                if mask[r] & (1 << c):
                    continue
                # 중복된 타겟인지 검사
                if (r, c) in shoot:
                    break
                shoot.add((r, c))
                # 타겟을 하나 정했다면 그만
                break

        # 적 제거
        for r, c in shoot:
            mask[r] |= (1 << c)
            cnt += 1

        # 적 제거 카운트 갱신
        ans = max(cnt, ans)
        if ans == max_ans:
            found = True


T = int(input())
for t in range(1, T + 1):
    N, M, D = map(int, input().split())
    e_cum_cnt = [0] * N # 턴별 남은 적
    e_priority = [[] for _ in range(M)]  # 궁수별 모든 적에 대한 공격 우선순위 (거리, 열, 성벽 도달까지 남은 턴=행)
    # O(NM^2)
    total_e = 0
    for i in range(N):
        for j, e in enumerate(list(map(int, input().split()))):
            if e == 0:
                continue
            for k in range(M):
                e_priority[k].append((distance(i, j, N, k), j, N - i - 1))
            total_e += 1
        e_cum_cnt[i] = total_e
    e_cum_cnt.reverse()

    for k in range(M):
        e_priority[k].sort()

    # O(MC3 * sim)
    # 총 턴 수 * 궁수 수와 총 적의 수 중 최소값
    max_ans = min(N * 3, total_e)
    ans = 0
    found = False
    for i in range(M-2): # 첫번째 궁수자리
        for j in range(i+1, M-1): # 두번째 궁수자리
            for k in range(j+1, M): # 세번째 궁수자리
                simulate(i, j, k)
                if found:
                    break
            if found:
                break
        if found:
            break
    print(f"#{t} {ans}")