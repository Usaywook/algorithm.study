def solve():
    N = int(input())    
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))
        
     # K=1부터 5까지 시도
    for k in range(1, 6):
        if feasible(k, packets):
            return k        
    return -1

def dominates(a, b):
    """상태 a가 상태 b를 우위하는지 판정 (즉, a의 모든 원소가 b보다 작거나 같으면 True)"""
    return all(x <= y for x, y in zip(a, b))

def feasible(K, packets):
    # 초기 상태: 모든 cpu가 free (finish time 0)     
    states = {(0,) * K}
    
    # 모든 패킷에 대해서 dp table 업데이트
    for T, L in packets:
        # 패킷 별 후보 상태 정의
        new_states = dict()       
        # 모든 정렬된 상태에 대해서 branch 순회
        for state in states:
            # 모든 cpu에 대해서 상태 업데이트 및 dp value 계산
            for j in range(K):
                f = state[j]                
                if f > T + 10 - L:
                    # 조건 불만족
                    continue
                elif f <= T:
                    # free
                    new_f = T + L
                else:
                    # busy
                    new_f = f + L
                                
                new_state = list(state)
                new_state[j] = new_f
                new_state.sort()
                new_state = tuple(new_state)
                
                # new_state를 저장할 때, 우위 판정을 통해 pruning
                # 우위 여부는 모든 cpu의 finish time이 작은지에 따라서 결정
                dominated = False
                to_remove = []
                for s in new_states:
                    if dominates(s, new_state):
                        dominated = True
                        break                    
                    if dominates(new_state, s):
                        to_remove.append(s)
                # new state보다 좋은 것이 이미 있다면 제외
                if dominated:
                    continue                
                # new state보다 안좋은 state모두 제거
                for s in to_remove:
                    del new_states[s]                    
                new_states[new_state] = True
        # 모든 branch 제외된 경우
        if not new_states:
            return False
        states = new_states
    # leaf까지 branch 있다면
    return True                     
                    
if __name__ == '__main__':
    import sys
    sys.stdin = open("input.txt", 'r')

    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)