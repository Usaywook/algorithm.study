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
        res = segment[0]
        cnt = 1
        while cnt < len(segment):
            x = segment[cnt]
            if x == "+":
                cnt += 1
                res += segment[cnt]
            elif x == "-":
                cnt += 1
                res -= segment[cnt]
            elif x == "*":
                cnt += 1
                res *= segment[cnt]
            cnt += 1
        return res

    start = -1
    new_arr = []
    for i in range(len(arr)):
        x = arr[i]
        if start == -1 and x == "(":
            start = i + 1
        elif start != -1 and x == ")":
            end = i
            new_arr.append(get_ans(arr[start:end]))
            start = -1
        elif start == -1:
            new_arr.append(x)

    return get_ans(new_arr)

def search(i, flag=False, p_ind=0, new_arr = []):
    global ans
    if i == N:
        res = calculate(new_arr)
        ans = max(ans, res)
        # print(f"{new_arr} {res}")
        return

    x = array[i]
    if isinstance(x, int):
        is_close = False
        if flag:
            new_arr.append(x)
            new_arr.append(")")
            search(i+1, False, p_ind, new_arr)
            new_arr.pop()
            new_arr.pop()
            if i - p_ind == 2:
                is_close = True
            if i == N - 1:
                is_close = True

        elif not flag and i < N-2:
            new_arr.append("(")
            new_arr.append(x)
            search(i + 1, True, i, new_arr)
            new_arr.pop()
            new_arr.pop()

        if not is_close:
            new_arr.append(x)
            search(i+1, flag, p_ind, new_arr)
            new_arr.pop()

    else:
        new_arr.append(x)
        search(i + 1, flag, p_ind, new_arr)
        new_arr.pop()

ans = -2**31
search(0)
print(ans)
