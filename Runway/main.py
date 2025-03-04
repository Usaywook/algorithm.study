import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    # for row in array:
    #     print(row)
    
    cnt = 0
    # 가로 검사
    # print("check horizontal", X)
    for i in range(N):        
        is_runway = True
        p = 0
        q = 0
        for j in range(1, N):
            prev, cur = array[i][j-1], array[i][j]
            diff = cur - prev
            if diff == 0: # 평지
                if q != 0 and j - q + 1 >= X:
                    is_runway = True
                    p = j
                    # print(array[i][j], "case 1.1", is_runway)  
                # else:
                #     print(array[i][j], "case 1.2", is_runway)           
            elif diff == 1: # 오르막
                if j - p < X:
                    is_runway = False
                    # print(array[i][j], "case 2.1", is_runway)
                    break
                else:
                    p = j
                    # print(array[i][j], "case 2.2", is_runway)
            elif diff == -1: # 내리막
                if not is_runway:
                    # print(array[i][j], "case 3.1", is_runway) 
                    break
                else:
                    q = j
                    is_runway = False
                    # print(array[i][j], "case 3.2", is_runway)                      
            else:
                is_runway = False
                # print(array[i][j], "case 4", is_runway)
                break
        
        # print(i, is_runway)
        cnt += int(is_runway)
    
    # 세로 검사
    # print("check vertical", X)
    for j in range(N):        
        is_runway = True
        p = 0
        q = 0
        for i in range(1, N):
            prev, cur = array[i-1][j], array[i][j]
            diff = cur - prev
            if diff == 0: # 평지
                if q != 0 and i - q + 1 >= X:
                    is_runway = True
                    p = i
                    # print(array[i][j], p, i, "case 1.1", is_runway)  
                # else:
                #     print(array[i][j], p, i, "case 1.2", is_runway)           
            elif diff == 1: # 오르막
                if i - p < X:
                    is_runway = False
                    # print(array[i][j], p, i, "case 2.1", is_runway)
                    break
                else:
                    p = i
                    # print(array[i][j], p, i, "case 2.2", is_runway)
            elif diff == -1: # 내리막
                if not is_runway:
                    # print(array[i][j], p, i, "case 3.1", is_runway) 
                    break
                else:
                    q = i
                    is_runway = False
                    # print(array[i][j], p, i, "case 3.2", is_runway)                      
            else:
                is_runway = False
                # print(array[i][j], p, i, "case 4", is_runway)
                break
        # print(j, is_runway)
        cnt += int(is_runway)
    
    print(f'#{test_case} {cnt}')
    # break
    