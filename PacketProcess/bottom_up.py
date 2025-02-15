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
    # 초기 상태: 모든 CPU가 finish time 0, waiting sum 0
    t, L = packets[0]
    init_processes = [0] * cpu_num
    init_queues = [0] * cpu_num
    init_processes[0] = t + L
    
    # dp_state는 (processes, queues)를 나타내는 상태
    # 여기서는 단계별로 이전 상태만 유지하여 메모리 사용량을 줄임
    prev_states = set()
    prev_states.add((tuple(init_processes), tuple(init_queues)))
    
    # dp: rolling 방식, 이전 단계의 상태만 유지
    for i in range(1, n):
        t, L = packets[i]
        current_states = set()
        for (processes, queues) in prev_states:
            proc_list = list(processes)
            
            # 즉각 처리 경우: 가능한 첫 CPU만 선택 (for-loop 후 break)
            for cpu in range(cpu_num):
                if proc_list[cpu] <= t:
                    new_proc = list(proc_list)
                    new_proc[cpu] = t + L
                    current_states.add((tuple(new_proc), queues))
                    break  # 첫 유효 CPU만 고려
            
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
                current_states.add((processes, tuple(new_queues)))
        if not current_states:
            return False
        # 이전 단계 상태 집합을 현재 상태 집합으로 갱신 (rolling update)
        prev_states = current_states
    return True

if __name__ == '__main__':
    sys.stdin = open("input.txt", 'r')
    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)