def isPlace(x, y):
    # 2x2 블록이 범위 내에 있고 모두 0이어야 함
    if x + 1 >= H or y + 1 >= W:
        return False
    if wafer[x][y] or wafer[x+1][y] or wafer[x][y+1] or wafer[x+1][y+1]:
        return False
    return True      
    
def solve():
    global H, W, wafer, dp
    H, W = map(int, input().split())
    wafer = []
    for i in range(H):
        wafer.append(list(map(int, input().split())))
    
    # dp[bit][y] : y열의 상태(bitmask)에서 얻은 최대 chip 개수 (bit: 각 행의 상태, 0이면 사용가능, 1이면 이미 사용 혹은 장애)
    # 일반적인 해법: 열 y의 상태를 튜플로 표현, but 상태가 이진 수로 표현된다면 bitmasking 활용.
    # dp = {}  # 키: (y, state_tuple), 값: 현재까지 배치한 칩 수 (cnt)        
    dp = [[-1] * W for _ in range(1 << H)]
    ans = 0    
    def dfs(x, y, cnt):        
        nonlocal ans       
        # 현재 열에서 마지막 행까지 검사했으면 다음 열로 넘어감
        if x >= H - 1:
            x = 0
            y += 1
        # 기판에서 2열을 사용해야 하므로 마지막 열은 사용할 수 없음.
        if y == W - 1:
            ans = max(ans, cnt)
            return

        # 새로운 열의 시작 (x==0)에서 해당 열의 상태를 비트마스크로 저장하여 메모이제이션
        if x == 0:
            # 일반적인 해법: 열 y의 상태를 튜플로 표현
            # col_state = tuple(wafer[i][y] for i in range(H))
            # key = (y, col_state)
            # if dp.get(key, -1) >= cnt:
            #     return
            # dp[key] = cnt            
            bit = 0
            for i in range(H):
                # wafer[i][y]가 1이면 해당 행은 사용 불가(또는 이미 사용된 상태)
                bit |= (wafer[i][y] << i)
            # 같은 상태에 이미 더 큰 cnt 있다면 제외
            if dp[bit][y] >= cnt:
                return
            dp[bit][y] = cnt            

        # 해당 위치에 2x2 칩을 놓을 수 있다면 놓고 재귀 호출
        if isPlace(x, y):
            # 칩 배치: 2x2 영역을 1로 마킹 (이미 사용되었거나 장애가 있는 상태)
            wafer[x][y] = wafer[x+1][y] = wafer[x][y+1] = wafer[x+1][y+1] = 1
            dfs(x + 2, y, cnt + 1)
            # 백트래킹: 원상복구
            wafer[x][y] = wafer[x+1][y] = wafer[x][y+1] = wafer[x+1][y+1] = 0
        # 칩을 놓지 않고 다음 행으로 넘어감
        dfs(x + 1, y, cnt)
    dfs(0, 0, 0)    
    print(ans)

if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt")
    T = int(input())
    for t in range(T):        
        print(f"#{t+1}", end=" ")
        solve()                