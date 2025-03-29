import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))


    def is_feasible(k, i, time):
        if i == N:
            return True

        key = (i, tuple(sorted(time)))
        if key in cache:
            return cache[key]

        begin, process = packets[i]

        for cpu in range(k):
            queue = time[cpu] - begin
            if queue + process > 10:
                continue

            end = time[cpu]
            if queue > 0:
                time[cpu] += process
            else:
                time[cpu] = begin + process

            if is_feasible(k, i + 1, time):
                cache[key] = True
                return True

            time[cpu] = end  # 백트래킹

        cache[key] = False
        return False

    ans = -1
    for k in range(1, 6):
        time = [0] * k
        cache = {}
        if is_feasible(k, 0, time):
            ans = k
            break
    print(f"#{t} {ans}")