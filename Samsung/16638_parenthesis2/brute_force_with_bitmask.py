import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().strip())
expr = input().strip()

# 숫자와 연산자를 분리 (문자열 형태로 저장하여 이후 재결합이 용이하도록 함)
nums = []
ops = []
for i, ch in enumerate(expr):
    if i % 2 == 0:
        nums.append(ch)  # 숫자는 문자열로 저장
    else:
        ops.append(ch)

M = len(ops)  # 연산자 개수
ans = -2 ** 31


def operate(a, op, b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def evaluate(mask):
    # mask의 각 비트는 해당 연산자에 괄호를 사용할지 여부를 결정 (인접 1 불가)
    # temp_nums와 temp_ops는 괄호 적용 후 식을 재구성하기 위한 복사본입니다.
    temp_nums = nums[:]  # 각 원소는 문자열
    temp_ops = ops[:]

    # 오른쪽부터 처리하여 인덱스 문제를 피합니다.
    for i in range(M - 1, -1, -1):
        if mask & (1 << i):
            # i번째 연산자에 괄호 사용 → temp_nums[i] op temp_nums[i+1]를 먼저 계산
            res = str(operate(temp_nums[i], temp_ops[i], temp_nums[i + 1]))
            temp_nums[i] = res
            # 해당 연산자와 오른쪽 숫자를 제거
            del temp_nums[i + 1]
            del temp_ops[i]

    # 이제 temp_nums와 temp_ops로 구성된 식은 괄호 처리가 완료된 상태입니다.
    # 문제 조건에 따라, 남은 식은 "곱셈이 덧셈/뺄셈보다 우선"이므로
    # 먼저 모든 곱셈을 처리하고, 그 후 왼쪽부터 덧셈/뺄셈을 순차적으로 계산합니다.

    # 1단계: 곱셈 처리
    new_nums = [int(temp_nums[0])]
    new_ops = []
    for i, op in enumerate(temp_ops):
        if op == '*':
            new_nums[-1] = new_nums[-1] * int(temp_nums[i + 1])
        else:
            new_ops.append(op)
            new_nums.append(int(temp_nums[i + 1]))

    # 2단계: 덧셈과 뺄셈을 왼쪽부터 계산
    result = new_nums[0]
    for i, op in enumerate(new_ops):
        if op == '+':
            result += new_nums[i + 1]
        else:  # op == '-'
            result -= new_nums[i + 1]
    return result


# 모든 mask (0부터 2^M-1) 중에서, 인접한 연산자에 동시에 괄호가 있는 경우는 제외
for mask in range(1 << M):
    if mask & (mask << 1):
        continue
    res = evaluate(mask)
    ans = max(ans, res)
print(ans)