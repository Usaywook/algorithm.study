import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    # 가로 검사
    for i in range(N):        
        is_runway = True
        is_down = False
        is_ramp = False
        p = 0
        q = 0        
        for j in range(1, N):
            prev, cur = array[i][j-1], array[i][j]
            diff = cur - prev
            if diff == 0: # 평지
                if is_down and j - q + 1 >= X:
                    is_runway = True
                    is_down = False
                    p = j        
            elif diff == 1: # 오르막
                if is_down:
                    is_runway = False  
                    break
                if j - p < X:
                    is_runway = False
                    break
                else:
                    p = j
            elif diff == -1: # 내리막
                if is_down:
                    is_runway = False  
                    break
                else:
                    q = j
                    is_down = True
                    is_runway = False                    
            else:
                is_runway = False
                break
        cnt += int(is_runway)
    
    # 세로 검사
    for j in range(N):        
        is_runway = True
        is_down = False
        p = 0
        q = 0
        for i in range(1, N):
            prev, cur = array[i-1][j], array[i][j]
            diff = cur - prev
            if diff == 0: # 평지
                if is_down and i - q + 1 >= X:
                    is_runway = True
                    is_down = False
                    p = i        
            elif diff == 1: # 오르막
                if is_down:
                    is_runway = False  
                    break
                if i - p < X:
                    is_runway = False
                    break
                else:
                    p = i
            elif diff == -1: # 내리막
                if is_down:
                    is_runway = False  
                    break
                else:
                    q = i
                    is_down = True
                    is_runway = False                    
            else:
                is_runway = False
                break
        cnt += int(is_runway)
    
    print(f'#{test_case} {cnt}')
    