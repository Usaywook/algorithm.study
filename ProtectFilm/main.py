import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    cells = []
    for _ in range(D):
        cells.append(list(map(int, input().split())))

    def isPass():
        for j in range(W):
            is_pass = False
            for i in range(D):
                if  i == 0:
                    counter = 1
                else :
                    if cells[i-1][j] == cells[i][j]:
                        counter += 1
                    else:
                        counter = 1
                if counter >= K:
                    is_pass = True
                    break

            if not is_pass:
                return False
        return True


    def search(i, cnt):
        global ans
        if K == 1:
            ans = min(ans, cnt)
            return

        if cnt > ans:
            return

        # 통과한다면 cnt 반환
        if isPass():
            ans = min(ans, cnt)
            return

        if i == D:
            return

        # i 번째에 약품 주입 안함
        search(i + 1, cnt)

        for x in range(2):
            # i 번째에 x 약품 주입
            origin = []
            for j in range(W):
                origin.append(cells[i][j])
                cells[i][j] = x

            # 재귀 호출
            search(i + 1, cnt+1)

            # 롤백
            for j in range(W):
                cells[i][j] = origin[j]

    ans = D
    search(0, 0)

    print(f"#{t} {ans}")
