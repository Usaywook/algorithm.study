import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):        
        is_runway = True
        ramp_p = -1
        for j in range(1, N):
            if array[i][j-1] - array[i][j] == 0:
                if ramp_p != -1:
                    if j - ramp_p + 1 < X:
                        is_runway = False
                        print(j, is_runway, "case 1")
                    else:
                        is_runway = True
                        ramp_p = -1        
                        print(j, is_runway, "case 2")
                else:
                    print(j, is_runway, "case 3")
                
            elif abs(array[i][j-1] - array[i][j]) == 1:
                if ramp_p == -1:
                    ramp_p = j
                    is_runway = False
                    print(j, is_runway, "case 4")
                else:
                    if j - ramp_p < X:
                        # ramp_p = j
                        is_runway = False
                        print(j, is_runway, "case 5")
                    else:
                        ramp_p = j                   
                        print(j, is_runway, "case 6")       
            else:
                is_runway = False
                print(j, is_runway, "case 7")
                break
        print(i, is_runway)
        print()
    break
    