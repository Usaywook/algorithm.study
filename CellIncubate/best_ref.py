import sys
sys.stdin = open("input.txt", "r")

T=int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for case in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    matrix = [[0] *(M+K) for _ in range(N+K)]
    cell_list = [[] for _ in range(11)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                matrix[i+K//2][j+K//2] = arr[i][j]
                cell_list[arr[i][j]].append((i+K//2,j+K//2))
    for time in range(1,K+1):
        for life in range(10,0,-1):
            if time%(life+1) !=0:
                continue
            survive = []
            for val in cell_list[life]:
                if (K-time)<(life-1):
                    survive.append(val)
                for k in range(4):
                    nx = val[0]+dx[k]
                    ny = val[1]+dy[k]
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = life
                        survive.append((nx,ny))
            cell_list[life] = survive
            
    result = 0
    for i in cell_list:
        result+=len(i)
    print(f'#{case} {result}')