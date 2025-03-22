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

def search(i, p_cnt=0, new_arr = []):
    global ans
    if i == -1:
        # print(f"start {new_arr[::-1]}")
        res = calculate(new_arr[::-1])
        ans = max(ans, res)
        print(f"leaf: {new_arr[::-1]} {res}")
        # print()
        return

    x = array[i]
    new_arr.append(x)
    if isinstance(x, str):
        if x == "*":
            new_arr.append(")")
            search(i - 1, p_cnt + 1, new_arr)
            new_arr.pop()
        elif p_cnt > 0 and (x == "+" or x == "-"):
            new_arr.append(array[i-1])
            new_arr.append("(")
            if i - 2 < 0:
                for k in range(p_cnt - 1):
                    new_arr.append("(")
            search(i - 2, p_cnt - 1, new_arr)
            if i - 2 < 0:
                for k in range(p_cnt - 1):
                    new_arr.pop()
            new_arr.pop()
            new_arr.pop()

        if not (i - 2 < 0 and p_cnt > 0):
            search(i - 1, p_cnt, new_arr)

    else:
        search(i - 1, p_cnt, new_arr)

    new_arr.pop()

ans = -2**31
search(N-1)
print(ans)
