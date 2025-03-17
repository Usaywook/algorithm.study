arr = [2,-1, -2, 1, -4, 2, 8]
# arr = [3, -1, 4, -2, 2, -3, 6]
N = len(arr)


def max_non_overlapping_subarrays_diff():
    """
    Kadane’s Algorithm(카데인 알고리즘)과 유사한 DP 기반 최적화 기법
    DP + 그리디(최적 부분 구조 활용) + Kadane's Algorithm 변형
    """
    n = len(arr)

    # Step 1: 누적 합 배열 생성
    # prefix_sum[q] - prefix_sum[p] 로 배열의 [p, q) 범위의 부분합을 O(1) 에 구할 수 있음
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    # Step 2: 첫 번째 부분 배열의 최소 합 찾기
    # left_min[i]는 [0,i] 에서 최소 부분합을 저장
    # min_prefix는 [0,i] 에서 누적합 중 최대값이고, 최소 부분합 left_min을 구하는데 사용된다.
    # [0,i] 에서 최소 부분합은 i까지 누적합 - i까지 누적합 중 최대값
    INF = 10000 * n + 1 # 2**(-31) + 1
    left_min = [INF] * n
    min_prefix = 0
    for i in range(n):
        left_min[i] = min(left_min[i - 1] if i > 0 else INF, prefix_sum[i + 1] - min_prefix)
        min_prefix = max(min_prefix, prefix_sum[i + 1])

    # Step 3: 두 번째 부분 배열을 고려하며 최댓값 찾기
    # max_suffix는 [j, n) 에서 최대 부분합
    # left_min[j - 1]은 [0, j) 에서 최소 부분합
    # max_diff은 [0,n) 에서 [j, n) 에서 최대 부분합 - [0, j) 에서 최소 부분합 중 최대값
    max_diff = max_suffix = - INF
    for j in range(n - 1, 0, -1):
        max_suffix = max(max_suffix, prefix_sum[n] - prefix_sum[j])
        max_diff = max(max_diff, max_suffix - left_min[j - 1])

    return max_diff

print(max_non_overlapping_subarrays_diff())  # 예상 출력값