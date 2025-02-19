import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(T):
    N, O, M  = map(int, input().split())
    numbers = list(input().split())
    operators = list(input().split())
    W = int(input())
    
    print(f"#{t+1}", end=" ")
    
    def getCandidate(K, ans=[]):
        if len(ans) > 1 and ans[0] == '0':            
            return
        
        if len(ans) > K-1:                    
            yield ''.join(ans)       
            return                
                
        for number in numbers:
            yield from getCandidate(K, ans + [number])
    
    candidates = [cand for k in range(1, 4) for cand in getCandidate(k)]
    states = [-1] * 1000    
          
    queue = deque(list(zip(map(list, candidates[:]), map(int, candidates[:]), [1] * len(candidates))))
    while queue:
        select, number, depth = queue.popleft()             
        # condition
        if len(select) > M or number < 0 or number > 999:
            continue
        # pruning
        if states[number] > len(select):
            continue
        # update states
        states[number] = len(select) if depth == 1 else len(select) + 1            
        # base case
        if number == W:
            # print(select)
            break 
        # select operator
        for operator in operators:
            # select number
            for candidate in candidates:                    
                select_number = int(candidate)     
                select_number_list = list(map(list, candidate))           
                if operator == '1':                                        
                    queue.append((select + ['+'] + select_number_list, number + select_number, depth + 1))
                elif operator == '2':
                    queue.append((select + ['-'] + select_number_list, number - select_number, depth + 1))
                elif operator == '3':
                    queue.append((select + ['*'] + select_number_list, int(number * select_number), depth + 1))
                elif operator == '4':                        
                    if select_number == 0:
                        continue
                    queue.append((select + ['/'] + select_number_list, int(number / select_number), depth + 1))    
    print(states[W])                                    