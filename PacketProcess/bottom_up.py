import sys

def solve():
    N = int(input())
    packets = [tuple(map(int, input().split())) for _ in range(N)]
    
    for cpu_num in range(1, 6):
        if solve_bottom_up(cpu_num, packets):
            return cpu_num
    return -1

def dominates(state1, state2):
    """
    state: (processes, queues)
    state1 dominates state2 if for every CPU, state1's finish time <= state2's finish time 
    and waiting sum <= state2's waiting sum, with at least one strict inequality.
    """
    processes1, queues1 = state1
    processes2, queues2 = state2
    strict = False
    for i in range(len(processes1)):
        if processes1[i] > processes2[i] or queues1[i] > queues2[i]:
            return False
        if processes1[i] < processes2[i] or queues1[i] < queues2[i]:
            strict = True
    return strict

def add_state(states, new_state):
    """
    states: set of states (each state is a tuple: (processes, queues))
    new_state: candidate state to add.
    만약 new_state가 기존 상태에 의해 dominated 되면 추가하지 않고,
    new_state가 기존 상태들을 dominated 한다면 그 상태들을 제거한 후 추가.
    """
    to_remove = set()
    for st in states:
        if dominates(st, new_state):
            # new_state is no better than st -> skip adding
            return
        if dominates(new_state, st):
            to_remove.add(st)
    states.difference_update(to_remove)
    states.add(new_state)

def solve_bottom_up(cpu_num, packets):
    n = len(packets)
    # 초기 상태: 모든 CPU의 finish time와 waiting sum이 0
    t, L = packets[0]
    init_processes = [0] * cpu_num
    init_queues = [0] * cpu_num
    # 첫 패킷은 cpu0에서 즉각 처리
    init_processes[0] = t + L
    
    # prev_states: 현재까지 도달 가능한 상태 집합
    prev_states = set()
    prev_states.add((tuple(init_processes), tuple(init_queues)))
    
    # 각 단계마다 rolling dp를 수행
    for i in range(1, n):
        t, L = packets[i]
        current_states = set()
        for (processes, queues) in prev_states:
            proc_list = list(processes)
            que_list = list(queues)
            # [1] 즉각 처리: 가능한 첫 CPU만 선택 (for-loop 후 break)
            for cpu in range(cpu_num):
                if proc_list[cpu] <= t:
                    new_proc = list(proc_list)
                    new_proc[cpu] = t + L
                    # 즉각 처리 시 waiting 값은 그대로
                    add_state(current_states, (tuple(new_proc), tuple(que_list)))
                    break  # 첫 유효 CPU만 고려
            
            # [2] 대기 처리: 모든 CPU 중 waiting 시간이 최소인 CPU 선택
            min_length = 11
            min_cpu = -1
            for cpu in range(cpu_num):
                if proc_list[cpu] <= t:
                    continue  # 즉각 처리 가능한 경우는 대기 branch에서 고려하지 않음
                packet_length = (proc_list[cpu] - t) + que_list[cpu] + L
                if packet_length < min_length:
                    min_length = packet_length
                    min_cpu = cpu
            if min_cpu != -1 and min_length <= 10:
                new_queues = list(que_list)
                new_queues[min_cpu] += L
                add_state(current_states, (processes, tuple(new_queues)))
        if not current_states:
            return False
        prev_states = current_states  # rolling update
    return True

if __name__ == '__main__':
    sys.stdin = open("input.txt", 'r')
    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)