import sys
sys.stdin = open("input.txt", 'r')

from collections import deque

T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))

    def feasible(K):
        memory = set()
        queue = deque()
        queue.append((0, 0, [0] * K))  # (pidx, prev_time, wait_times)

        while queue:
            pidx, prev, wtimes = queue.popleft()
            if pidx == len(packets):
                return True

            cur, ptime = packets[pidx]

            # cpu 별 남은 대기 시간 갱신
            diff = cur - prev
            wtimes = [max(w - diff, 0) for w in wtimes]

            # 이미 탐색한 상태 캐싱으로 처리
            wtimes.sort()
            key = (pidx, tuple(wtimes))
            if key in memory:
                continue
            memory.add(key)

            for i in range(K):
                # 대기 시간이 10초 넘어가면 제외
                if wtimes[i] + ptime > 10:
                    continue
                # 대기시간 업데이트 및 다음 노드 탐색
                new_wtimes = wtimes[:]
                new_wtimes[i] += ptime
                queue.append((pidx + 1, cur, new_wtimes))

        return False

    ans = -1
    for k in range(1, 6):
        time = [0] * k
        if feasible(k):
            ans = k
            break
    print(f"#{t} {ans}")