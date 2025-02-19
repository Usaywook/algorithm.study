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
    
    def getCandidate(K, ans=''):
        if len(ans) > 1 and ans[0] == '0':            
            return
        
        if len(ans) > K-1:                    
            yield ans
            return                
                
        for number in numbers:
            yield from getCandidate(K, ans + number)
    
    def getCandidates():
        for k in range(1, 4):
            for cand in getCandidate(k):
                yield cand
                    
    states = {}
    queue = deque()
    candidates_list = list(getCandidates())
    for candidate in candidates_list:
        num = int(candidate)
        queue.append((num, len(candidate), 1))  # (숫자, 입력한 길이, 연산 횟수)
    
    while queue:
        number, length, depth = queue.popleft()                     
        if number in states and states[number] <= length:                   
            continue      
        
        # update states
        states[number] = length if depth == 1 else length + 1            
        # base case
        if number == W:            
            break 
        # select operator
        for operator in operators:
            # select number
            for candidate in candidates_list:                    
                select_number = int(candidate)                       
                if operator == '1':                                        
                    ans_number = number + select_number
                elif operator == '2':
                    ans_number = number - select_number
                elif operator == '3':
                    ans_number = int(number * select_number)
                elif operator == '4':                        
                    if select_number == 0:
                        continue 
                    ans_number = int(number / select_number)           
                ans_length = length + len(candidate) + 1
                # condition
                if ans_length > M or ans_number < 0 or ans_number > 999:
                    continue
                # pruning
                if ans_number in states and states[ans_number] <= ans_length:
                    continue
                queue.append((ans_number, length + len(candidate) + 1, depth + 1))    
                
    if W in states:        
        print(states[W])                                    
    else:
        print(-1)