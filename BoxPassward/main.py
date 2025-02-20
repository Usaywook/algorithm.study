import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    M = N // 4
    numbers = input()
    candidates = set()
    num = ''
    for i in range(M):
        for j in range(N):
            k = -i + j 
            x = numbers[k]
            num += x 
            if (i * N + j) % M == M - 1:
                candidates.add(num)
                num = ''        
    print(f"#{t+1}", end=" ")
    print(int(sorted(candidates, reverse=True)[K-1], 16))