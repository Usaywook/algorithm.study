import sys
sys.stdin = open("input.txt", "r")

import heapq 

di = (0, -1, 1, 0, 0)
dj = (0, 0, 0, -1, 1)

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int, input().split())
    states = [] 
    for k in range(K):
        i, j, n, k = map(int, input().split())
        states.append((n, i, j, k))    
        
    heapq.heapify(states)     
    
    for _ in range(M):
        new_states = []
        visited = dict()
        while states:            
            n, i, j, k = heapq.heappop(states)
            ni = i + di[k]
            nj = j + dj[k]
            is_bound = True
            if ni == 0:
                nk = 2
            elif ni == N-1:
                nk = 1
            elif nj == 0:
                nk = 4
            elif nj == N-1:
                nk = 3
            else:
                is_bound = False
                
            if is_bound:            
                new_states.append((n // 2, ni, nj, nk))
                visited[(ni, nj)] = len(new_states)-1
            else:
                if (ni, nj) in visited.keys():
                    ind = visited[(ni, nj)]                
                    new_states[ind] = (new_states[ind][0] + n, ni, nj, k)    
                else:
                    new_states.append((n, ni, nj, k))
                    visited[(ni, nj)] = len(new_states)-1
                                            
        heapq.heapify(new_states)
        states = new_states
    
    ans = sum([state[0] for state in states])
    print(f"#{t} {ans}")
        