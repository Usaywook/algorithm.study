import sys
from functools import lru_cache

def solve():
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)]
    
    for cpu_num in range(1, 6):
        if solve_top_down(cpu_num, packets):
            return cpu_num
    return -1

def solve_top_down(cpu_num, packets):
    n = len(packets)
    # 상태를 (i, processes, queues)로 정의합니다.
    # processes: 각 CPU의 finish time을 담은 tuple (길이: cpu_num)
    # queues: 각 CPU의 waiting sum을 담은 tuple (길이: cpu_num)
    @lru_cache(maxsize=None)
    def dp(i, processes, queues):
        if i == n:
            return True  # 모든 패킷 처리 완료
        
        t, L = packets[i]
        proc_list = list(processes)
        
        # [1] 즉각 처리 경우: 각 CPU에 대해 순서대로 확인 (가능한 첫 CPU만 사용)
        for cpu in range(cpu_num):
            if proc_list[cpu] > t:
                continue  # CPU가 아직 바쁘면 패스
            new_proc = list(proc_list)
            new_proc[cpu] = t + L
            if dp(i+1, tuple(new_proc), queues):
                return True
            # 첫 CPU에서 한 번 시도한 후 더 이상 immediate branch는 고려하지 않음
            break
        
        # [2] 대기 처리 경우: 모든 CPU 중 waiting 시간이 최소인 CPU만 선택
        min_length = 11
        min_cpu = -1
        for cpu in range(cpu_num):
            if proc_list[cpu] <= t:
                continue  # 즉각 처리 가능하면 대기 branch는 고려하지 않음
            # waiting 시간 = (CPU의 남은 처리시간) + (대기열 누적) + (새 패킷의 length)
            packet_length = (proc_list[cpu] - t) + queues[cpu] + L
            if packet_length < min_length:
                min_length = packet_length
                min_cpu = cpu
        if min_cpu != -1 and min_length <= 10:
            new_queues = list(queues)
            new_queues[min_cpu] += L
            if dp(i+1, processes, tuple(new_queues)):
                return True
        
        return False
    
    # 초기 상태: 모든 CPU가 finish time 0, waiting sum 0
    init_processes = tuple(0 for _ in range(cpu_num))
    init_queues = tuple(0 for _ in range(cpu_num))
    # 첫 패킷은 cpu0에서 즉각 처리하도록 설정 (코드의 흐름과 동일하게)
    t, L = packets[0]
    init_processes = list(init_processes)
    init_processes[0] = t + L
    return dp(1, tuple(init_processes), init_queues)

if __name__ == '__main__':
    sys.stdin = open("input.txt", 'r')
    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)