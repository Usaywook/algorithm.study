import sys

def solve():
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)]
    
    for cpu_num in range(1, 6):
        if solve_bottom_up(cpu_num, packets):
            return cpu_num
    return -1

def solve_bottom_up(cpu_num, packets):
    n = len(packets)
    # 각 상태는 (processes, queues)로 표현됩니다.
    # processes: 각 CPU의 finish time을 담은 tuple (길이: cpu_num)
    # queues: 각 CPU의 waiting sum을 담은 tuple (길이: cpu_num)
    # dp[i]는 첫 i개의 패킷까지 처리한 후 가능한 상태 집합
    dp = [set() for _ in range(n)]
    
    # 초기 상태: 첫 패킷은 cpu0에서 즉각 처리
    t, L = packets[0]
    init_processes = [0] * cpu_num
    init_queues = [0] * cpu_num
    init_processes[0] = t + L
    dp[0].add((tuple(init_processes), tuple(init_queues)))
    
    for i in range(1, n):
        t, L = packets[i]
        for (processes, queues) in dp[i-1]:
            proc_list = list(processes)
            # 즉각 처리 경우: 가능한 첫 CPU만 선택 (for-loop 후 break)
            for cpu in range(cpu_num):
                if proc_list[cpu] <= t:
                    new_proc = list(proc_list)
                    new_proc[cpu] = t + L
                    dp[i].add((tuple(new_proc), queues))
                    break
            
            # 대기 처리 경우: 모든 CPU 중 waiting 시간이 최소인 CPU 선택
            min_length = 11
            min_cpu = -1
            for cpu in range(cpu_num):
                if proc_list[cpu] <= t:
                    continue
                packet_length = (proc_list[cpu] - t) + queues[cpu] + L
                if packet_length < min_length:
                    min_length = packet_length
                    min_cpu = cpu
            if min_cpu != -1 and min_length <= 10:
                new_queues = list(queues)
                new_queues[min_cpu] += L
                dp[i].add((processes, tuple(new_queues)))
        if not dp[i]:
            return False
    return True

if __name__ == '__main__':
    sys.stdin = open("input.txt", 'r')
    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)