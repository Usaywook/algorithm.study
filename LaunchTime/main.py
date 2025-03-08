import sys
sys.stdin = open("input.txt", "r")

from collections import deque
from heapq import heappush

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # grid = []
    stairs = []
    people = []
    for i in range(N):
        row = list(map(int, input().split()))
        # grid.append(row)
        for j in range(N):
            e = row[j]
            if e == 1:
                people.append((i,j))
            elif e > 1:
                stairs.append((i,j,e))
            else:
                pass
                
    
    def getDistance(p, s):
        pi, pj = p[:2]
        si, sj = s[:2]
        return abs(pi - si) + abs(pj - sj)
    
    def findCompleteTime(choice):
        distances = {0: [], 1: []}
        for k, person in zip(choice, people):
            heappush(distances[k], getDistance(person, stairs[k]))
        
        processes = {0: deque(), 1: deque()}
        complete_time = 0
        for k, distance in distances.items():
            length = stairs[k][2]
            for d in distance:
                start = d + 1
                
                process = processes[k]
                pop_cnt = 0
                for p_time in process:
                    if start >= p_time:
                        pop_cnt += 1
                
                for _ in range(pop_cnt):        
                    process.popleft()
                        
                queue = 0
                if len(process) >= 3:
                    p_time = process.popleft()
                    queue = p_time - start
                    
                end = start + queue + length
                process.append(end)
                
                complete_time = max(complete_time, end)    
                # print(k, start, end, len(process), process)
                
        return complete_time
    
    global ans
    ans = 1000 #20 + 10 + 1 + 31*10
    
    def search(select=[]):
        if len(select) == len(people):
            global ans
            # print(select)
            time = findCompleteTime(select)
            ans = min(ans, time)
            return
        
        search(select + [0])
        search(select + [1])

    search()
    print(f"#{t} {ans}")