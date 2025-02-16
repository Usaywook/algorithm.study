def isPlace(x, y, state):
    # 2x2 블록이 범위 내에 있고 모두 0이어야 함
    if x + 1 >= H or y + 1 >= W:
        return False
    if state[x][y] or state[x+1][y] or state[x][y+1] or state[x+1][y+1]:
        return False
    return True      
    
def solve():
    global dp, wafer, H, W
    H, W = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(H)]

    # dp[bit][y] : y열의 상태(bitmask)에서 얻은 최대 chip 개수
    dp = [[-1] * W for _ in range(1 << H)]
    ans = 0

    # 스택 요소: (x, y, cnt, state)
    # state는 현재 웨이퍼 상태(2차원 리스트)를 의미하며, 백트래킹 효과를 위해 매 분기마다 복사함.
    stack = []
    # 초기 상태: 좌표 (0,0), 칩 개수 0, 초기 웨이퍼 상태
    initial_state = [row[:] for row in wafer]
    stack.append((0, 0, 0, initial_state))

    while stack:
        x, y, cnt, state = stack.pop()

        # 현재 열의 마지막 행을 넘어섰으면, 다음 열로 넘어감
        if x >= H - 1:
            x = 0
            y += 1

        # 마지막 열은 2x2 영역을 놓을 수 없으므로 결과 업데이트
        if y >= W - 1:
            ans = max(ans, cnt)
            continue

        # 새로운 열의 시작 (x==0)에서 해당 열의 상태를 비트마스크로 저장하여 메모이제이션
        if x == 0:
            bit = 0
            for i in range(H):
                bit |= (state[i][y] << i)
            if dp[bit][y] >= cnt:
                continue
            dp[bit][y] = cnt

        # 가지 1: (x, y) 위치에 2x2 칩을 놓는 경우 (놓을 수 있으면)
        if isPlace(x, y, state):
            # 현재 상태를 깊은 복사하여 칩을 놓은 새 상태 생성
            new_state = [row[:] for row in state]
            new_state[x][y] = new_state[x+1][y] = new_state[x][y+1] = new_state[x+1][y+1] = 1
            stack.append((x + 2, y, cnt + 1, new_state))
        # 가지 2: (x, y) 위치에 칩을 놓지 않고 넘어가는 경우
        stack.append((x + 1, y, cnt, state))
    
    print(ans)

if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt")
    T = int(input())
    for t in range(T):        
        print(f"#{t+1}", end=" ")
        solve()        