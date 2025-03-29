import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))

    def is_feasible(k, i, time):
        # base
        if i == N:
            return True

        begin, process = packets[i]

        min_queue, min_cpu = 11, -1
        # 찾기
        for cpu in range(k):
            # 가능성 체크
            queue = time[cpu] - begin
            if queue + process > 10:
                continue

            if queue > 0:
                # 대기시간 짧은 큐 찾기
                if queue < min_queue:
                    min_queue = queue
                    min_cpu = cpu
            else:
                # 즉각 처리
                end = time[cpu]
                time[cpu] = begin + process
                if is_feasible(k, i+1, time):
                    return True
                time[cpu] = end

        # 대기 후 처리
        if min_cpu != -1:
            end = time[min_cpu]
            time[min_cpu] += process
            if is_feasible(k, i+1, time):
                return True
            time[min_cpu] = end

        # 모든 경우 search 한 경우
        return False

    ans = -1
    for k in range(1, 6):
        time = [0] * k
        if is_feasible(k, 0, time):
            ans = k
            break
    print(f"#{t} {ans}")