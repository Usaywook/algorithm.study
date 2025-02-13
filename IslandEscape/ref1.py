import sys
sys.stdin = open('./input.txt', "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve():
    # Python에서 int형으로 0x3f3f3f3f를 그대로 쓰면 1061109567
    INF = 0x3f3f3f3f

    # 메모: cache[(now, visit, mode)] = 최대 높이
    #  now  : 직전에 사용한 박스(인덱스)
    #  visit: 비트마스크(이미 쓴 박스들)
    #  mode : 지금 박스가 어떤 "배치"로 놓였는지를 0/1/2 중 하나
    # 
    #  참고: C++ 원본코드는 (row,col)을 메모 인덱스에 쓰지 않지만,
    #        row,col 변화는 호출 인자로만 전달되며, 
    #        cache는 (now,visit,mode)만으로 관리합니다.
    #        원본 로직과 완전히 동일하게 하기 위해 여기서도 row,col은 메모 인덱스에 포함하지 않습니다.
    cache = {}

    def getLength(now, mode, row, col, visit):
        """
        now  : 직전에 사용한 박스 번호 (0이면 아직 아무것도 안 쌓음)
        mode : 직전 박스가 어떤 배치로 놓였는지(0~2)
        row, col : 현재 '남아있는' 밑면 크기
        visit: 이미 사용한 박스를 표시하는 비트마스크
        """
        # 파이썬에서는 (now, visit, mode)만으로 해시키 생성
        # (row, col)을 사용하지 않는 것은 C++ 코드와 동일한 로직
        # (C++ 코드도 cache[now][visit][mode]만 사용하고 row,col은 고려 안 함)
        key = (now, visit, mode)
        if key in cache:
            return cache[key]

        ret = 0  # 아직 높이 0으로 초기화

        # 다음에 배치할 박스 i를 순회
        for i in range(1, n+1):
            # 이미 쓴 박스라면 패스
            if (visit & (1 << (i-1))) != 0:
                continue

            # 새로 방문한 상태
            nv = visit | (1 << (i-1))

            # infos[i] = [가로, 세로, 높이] (정렬되어 a <= b <= c)
            # 여기서 "배치" 시도는 C++ 코드와 동일하게 3가지 if문을 체크
            #   1) (row >= a and col >= b) => 높이 c
            #   2) (row >= a and col >= c) => 높이 b
            #   3) (row >= b and col >= c) => 높이 a
            a, b, c = infos[i]

            # 배치 1: 밑면 (a,b), 높이 c
            if row >= a and col >= b:
                # 높이 c 쌓은 뒤, 다음 호출
                candidate = c + getLength(i, 0, a, b, nv)
                if candidate > ret:
                    ret = candidate

            # 배치 2: 밑면 (a,c), 높이 b
            if row >= a and col >= c:
                candidate = b + getLength(i, 1, a, c, nv)
                if candidate > ret:
                    ret = candidate

            # 배치 3: 밑면 (b,c), 높이 a
            if row >= b and col >= c:
                candidate = a + getLength(i, 2, b, c, nv)
                if candidate > ret:
                    ret = candidate

        cache[key] = ret
        return ret

    T = int(input())
    
    for tc in range(1, T+1):
        global n, infos
        n = int(input())

        # infos[i] = (a, b, c): 각 i번째 박스 (1 <= i <= n)
        # i=0 은 "가상의 박스"로, row=col=INF를 초기화하기 위한 용도
        # C++ 코드처럼 infos[0]은 매우 큰 밑면 설정
        infos = [[0, 0, 0] for _ in range(n+1)]
        infos[0] = [INF, INF, INF]

        # cache 초기화
        cache.clear()

        for i in range(1, n+1):
            x, y, z = map(int, input().split())
            # (x,y,z) 정렬 so that x <= y <= z
            arr = sorted([x, y, z])
            infos[i] = arr

        # C++ 원 코드:
        #   printf("#%d %d\n", tc, getLength(0, 0, INF, INF, 0));
        # 즉, 시작은 (now=0, mode=0, row=INF, col=INF, visit=0)
        ans = getLength(0, 0, INF, INF, 0)

        print(f"#{tc} {ans}")

solve()