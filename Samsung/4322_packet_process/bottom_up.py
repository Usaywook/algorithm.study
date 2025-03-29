import sys

sys.stdin = open("input.txt", 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))

    ans = -1
    for k in range(1, 6):
        states = {(0,) * k: True} # states = {(0,) * k}
        is_feasible = True
        for begin, process in packets:
            # 상태 탐색
            new_states = dict() # new_states = set()
            for time in states:
                for cpu, end in enumerate(time):
                    # cpu 가능 여부 체크
                    queue = end - begin
                    if queue + process > 10:
                        continue

                    if queue > 0:
                        # 대기 후 처리
                        new_end = end + process
                    else:
                        # 즉각 처리
                        new_end = begin + process

                    new_time = list(time)
                    new_time[cpu] = new_end
                    new_time.sort() # [a, b] 와 [b, a] 는 동일한 상태이므로 크게 상태 축소
                    new_time = tuple(new_time)

                    # 상태 축소
                    dominated = False
                    to_remove = []
                    def is_dominated(a, b):
                        return all(x <= y for x, y in zip(a, b))
                    for s in new_states:
                        # 이전 상태가 더 나으면 그만
                        if is_dominated(s, new_time):
                            dominated = True
                            break
                        # 새로운 상태가 더 나으면 이전 상태 제거
                        if is_dominated(new_time, s):
                            to_remove.append(s)
                    if dominated:
                        continue
                    for s in to_remove:
                        del new_states[s] # new_states.remove(s) O(n) - > O(1)
                    new_states[new_time] = True # new_states.add(new_time)

            if not new_states:
                is_feasible = False
                break

            # 상태 업데이트
            states = new_states

        if is_feasible and states:
            ans = k
            break

    print(f"#{t} {ans}")



