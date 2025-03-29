arr = [2,-1, -2, 1, -4, 2, 8]
# arr = [3, -1, 4, -2, 2, -3, 6]

n = len(arr)
INF = 10000 * n + 1
left_min = [INF] * n
left_min[0] = current_min = arr[0]
for i in range(1, n):
    current_min = min(arr[i], current_min + arr[i])  # 지금부터 새로 시작 or 이어서
    left_min[i] = min(left_min[i - 1], current_min)  # [0..i]까지 최소값 유지

right_max = [-INF] * n
right_max[-1] = current_sum = arr[-1]
for j in range(n - 2, -1, -1):
    current_sum = max(arr[j], current_sum + arr[j])
    right_max[j] = max(right_max[j + 1], current_sum)

max_diff = - INF
for k in range(1, n):
    # [k, n-1) 의 최대 부분합 - [0, k) 의 최소 부분합
    max_diff = max(right_max[k] - left_min[k-1], max_diff)

print(left_min)
print(right_max)
print(max_diff)