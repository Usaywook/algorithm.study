import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))


    def is_feasible(k, i, prev, wtime):
        if i == N:
            return True

        begin, process = packets[i]

        # cpu 별 남은 대기 시간 갱신
        diff = begin - prev
        wtime = [max(w - diff, 0) for w in wtime]

        # 이미 탐색한 상태 캐싱으로 처리
        wtime.sort()
        key = (i, tuple(wtime))
        if key in cache:
            return cache[key]

        for cpu in range(k):
            # 대기 시간이 10초 넘어가면 제외
            if wtime[cpu] + process > 10:
                continue

            # 대기시간 업데이트 및 다음 노드 탐색
            wait = wtime[cpu]
            wtime[cpu] += process
            if is_feasible(k, i + 1, begin, wtime):
                cache[key] = True
                return True
            wtime[cpu] = wait  # 롤백

        cache[key] = False
        return False

    ans = -1
    for k in range(1, 6):
        wtime = [0] * k
        cache = {}
        if is_feasible(k, 0, 0, wtime):
            ans = k
            break
    print(f"#{t} {ans}")