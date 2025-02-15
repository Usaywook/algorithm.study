import sys

def solve():
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)]
    for cpu_num in range(1, 6):
        if solve_bottom_up(cpu_num, packets):
            return cpu_num
    return -1

def dominates(state1, state2, cpu_num):
    """
    state는 (p0,...,p_{cpu-1}, q0,...,q_{cpu-1}) 형태의 튜플.
    state1 dominates state2 if for every cpu:
        state1[p] <= state2[p] and state1[q] <= state2[q]
    with at least one strict inequality.
    """
    strict = False
    for i in range(cpu_num):
        if state1[i] > state2[i]:
            return False
        if state1[i] < state2[i]:
            strict = True
    for i in range(cpu_num, 2*cpu_num):
        if state1[i] > state2[i]:
            return False
        if state1[i] < state2[i]:
            strict = True
    return strict

def add_state(states, new_state, cpu_num):
    """
    states: set of compressed states
    new_state: tuple of length 2*cpu_num
    기존 상태 중 new_state에 의해 dominated되는 상태들을 제거하고,
    만약 new_state가 다른 상태에 의해 dominated된다면 추가하지 않음.
    """
    to_remove = set()
    for s in states:
        if dominates(s, new_state, cpu_num):
            return  # new_state dominated by s -> skip
        if dominates(new_state, s, cpu_num):
            to_remove.add(s)
    states.difference_update(to_remove)
    states.add(new_state)

def solve_bottom_up(cpu_num, packets):
    n = len(packets)
    # 상태: (p0,...,p_{cpu-1}, q0,...,q_{cpu-1})
    # p_i: finish time of cpu i, q_i: waiting sum at cpu i.
    t0, L0 = packets[0]
    init_processes = [0] * cpu_num
    init_queues = [0] * cpu_num
    # 첫 패킷은 cpu0에서 즉각 처리
    init_processes[0] = t0 + L0
    init_state = tuple(init_processes + init_queues)
    
    prev_states = {init_state}
    
    for i in range(1, n):
        t, L = packets[i]
        current_states = set()
        for state in prev_states:
            # 복원: state = (p0,...,p_{cpu-1}, q0,...,q_{cpu-1})
            processes = list(state[:cpu_num])
            queues = list(state[cpu_num:])
            # [1] 즉각 처리: 가능한 첫 CPU만 선택
            for cpu in range(cpu_num):
                if processes[cpu] <= t:
                    new_processes = processes.copy()
                    new_processes[cpu] = t + L
                    new_state = tuple(new_processes + queues)
                    add_state(current_states, new_state, cpu_num)
                    break  # 첫 유효 CPU만 고려
            
            # [2] 대기 처리: 모든 CPU 중 waiting 시간이 최소인 CPU 선택
            min_packet_length = 11
            min_cpu = -1
            for cpu in range(cpu_num):
                if processes[cpu] <= t:
                    continue
                packet_length = (processes[cpu] - t) + queues[cpu] + L
                if packet_length < min_packet_length:
                    min_packet_length = packet_length
                    min_cpu = cpu
            if min_cpu != -1 and min_packet_length <= 10:
                new_queues = queues.copy()
                new_queues[min_cpu] += L
                new_state = tuple(processes + new_queues)
                add_state(current_states, new_state, cpu_num)
        if not current_states:
            return False
        # 추가: 우위 제거 후, 상태 수가 너무 많으면 상위 k개만 유지 (예: k = 10000)
        if len(current_states) > 10000:
            current_states = set(sorted(current_states)[:10000])
        prev_states = current_states
    return True

if __name__ == '__main__':
    sys.stdin = open("input.txt", 'r')
    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)