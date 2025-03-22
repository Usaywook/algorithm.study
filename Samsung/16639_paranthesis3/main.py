import sys
sys.stdin = open("input.txt", "r")

N = int(input())
array = []
for i, x in enumerate(input()):
    if i % 2 == 0:
        array.append(int(x))
    else:
        array.append(x)

def calculate(arr):
    def get_ans(segment):
        new_segment = []
        it = iter(segment)
        for x in it:
            if x == "*":
                p = new_segment.pop()
                q = next(it)
                r = p * q
                new_segment.append(r)
            else:
                new_segment.append(x)

        res = new_segment[0]
        cnt = 1
        while cnt < len(new_segment):
            x = new_segment[cnt]
            if x == "+":
                cnt += 1
                res += new_segment[cnt]
            elif x == "-":
                cnt += 1
                res -= new_segment[cnt]
            elif x == "*":
                cnt += 1
                res *= new_segment[cnt]
            cnt += 1
        return res

    def get_arr(segment):
        def is_parenthesis():
            for x in segment:
                if x == "(":
                    return True
            return False

        if is_parenthesis():
            start, end = -1, -1
            for i in range(len(segment)):
                x = segment[i]
                if x == "(":
                    start = i + 1
                elif x == ")":
                    end = i
                    break

            new_arr = []
            flag = False
            for i in range(len(segment)):
                if i < start - 1 or i > end:
                    new_arr.append(segment[i])
                elif not flag:
                    # print(f"segment: {segment[start:end]}")
                    new_arr.append(get_ans(segment[start:end]))
                    flag = True

            # print(f"new_arr: {new_arr}")
            return get_arr(new_arr)

        else:
            # print(f"segment: {segment}")
            return segment

    return get_ans(get_arr(arr))

def search(i, p_cnt = 0, new_arr = []):
    global ans
    global candidates
    if i == N:
        candidates.append(new_arr[:])
        res = calculate(new_arr)
        ans = max(ans, res)
        # print(f"leaf: {new_arr} {res}")
        # print()
        return

    K = (N - i) // 2

    x = array[i]
    if i % 2 == 0:  # 숫자 토큰인 경우
        if i != N - 1:
            # lookahead: i+1부터 연속된 연산자들이 모두 '*'인지 검사
            j = i + 1
            pure_mul = True
            while j < N and j % 2 == 1:
                if array[j] != "*":
                    pure_mul = False
                    break
                j += 2

            # pure multiplication 블록이 아니라면, 여러 쌍의 괄호 삽입 분기를 고려
            if not pure_mul:
                # 첫 토큰인 경우 괄호 삽입은 생략하도록 (원래 코드와 동일하게)
                max_k = K if i != 0 else K - 1
                for k in range(1, max_k + 1):
                    for _ in range(k):
                        new_arr.append("(")
                    new_arr.append(x)
                    search(i + 1, p_cnt + k, new_arr)
                    new_arr.pop()  # x 제거
                    for _ in range(k):
                        new_arr.pop()

            # 괄호 삽입 없이 진행하는 분기도 항상 고려
            new_arr.append(x)
            if i == N - 1:
                for _ in range(p_cnt):
                    new_arr.append(")")
                search(i + 1, 0, new_arr)
                for _ in range(p_cnt):
                    new_arr.pop()
            else:
                # 열린 괄호가 있다면 닫는 분기도 고려
                if p_cnt > 0:
                    new_arr.append(")")
                    search(i + 1, p_cnt - 1, new_arr)
                    new_arr.pop()
                search(i + 1, p_cnt, new_arr)
            new_arr.pop()
        else:
            # 마지막 숫자이면 단순히 처리
            new_arr.append(x)
            for _ in range(p_cnt):
                new_arr.append(")")
            search(i + 1, 0, new_arr)
            for _ in range(p_cnt):
                new_arr.pop()
            new_arr.pop()
    else:
        # 연산자 토큰은 그냥 추가
        new_arr.append(x)
        search(i + 1, p_cnt, new_arr)
        new_arr.pop()

ans = -2**31
candidates = []
search(0)
print(ans)
