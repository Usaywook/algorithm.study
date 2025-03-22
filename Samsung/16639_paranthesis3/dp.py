import sys
sys.stdin = open("input.txt", "r")

N = int(input().strip())
expr = input().strip()

# 숫자와 연산자를 분리합니다.
nums = []
ops = []
for i, ch in enumerate(expr):
    if i % 2 == 0:
        nums.append(int(ch))
    else:
        ops.append(ch)

n = len(nums)
# dp_max[i][j] : 식의 i번째 숫자부터 j번째 숫자까지 계산했을 때 가능한 최대값
# dp_min[i][j] : 식의 i번째 숫자부터 j번째 숫자까지 계산했을 때 가능한 최소값
dp_max = [[-2**31 for _ in range(n)] for _ in range(n)]
dp_min = [[2**31 for _ in range(n)] for _ in range(n)]

# 기저: 한 개의 숫자만 있는 경우
for i in range(n):
    dp_max[i][i] = nums[i]
    dp_min[i][i] = nums[i]

def operate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# 길이가 l+1인 부분식에 대해 모든 구간 [i, j] (j = i+l)에 대해 계산합니다.
for l in range(1, n):  # 부분식 길이 차이
    for i in range(n - l):
        j = i + l
        for k in range(i, j):
            # k는 i~j 사이에 있는 연산자의 인덱스 (nums[k] op[k] nums[k+1] 으로 나누는 위치)
            op = ops[k]
            # i~k 구간과 k+1~j 구간의 가능한 최소/최대값을 모두 고려
            a = operate(dp_max[i][k], op, dp_max[k+1][j])
            b = operate(dp_max[i][k], op, dp_min[k+1][j])
            c = operate(dp_min[i][k], op, dp_max[k+1][j])
            d = operate(dp_min[i][k], op, dp_min[k+1][j])
            dp_max[i][j] = max(dp_max[i][j], a, b, c, d)
            dp_min[i][j] = min(dp_min[i][j], a, b, c, d)

print(dp_max[0][n-1])