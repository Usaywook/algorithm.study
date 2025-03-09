import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M  = map(int, input().split())

    house = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                house.append((i, j))
    
    def getOperateCost(k):
        return k**2 + (k-1)**2
    
    def getDistance(x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)
    
    ans = 0
    max_count = len(house)
    for ci in range(N):
        for cj in range(N):
            # max_ck-1 = N 이므로 N+2
            for ck in range(1, N+2):
                operate_cost = getOperateCost(ck)
                count = 0
                if max_count * M - operate_cost < 0:
                    continue
                for hi, hj in house:                     
                    if getDistance(hi, hj, ci, cj) <= ck - 1:
                        count += 1         
                if count * M - operate_cost < 0:
                    continue                
                ans =  max(ans, count)
                    
    print(f"#{t} {ans}")
    