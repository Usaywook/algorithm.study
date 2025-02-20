from memory import memory_usage_decorator 
import sys
sys.stdin = open("input.txt", "r")

@memory_usage_decorator
def solve():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())

        M = N // 4
        numbers = input()
        candidates = set()        
        for i in range(M): # M번 회전
            for j in range(4): # 네 변의 숫자 추출
                start_idx = j * M                
                num = numbers[start_idx:start_idx + M]  # 슬라이싱 사용 (메모리 효율적)                
                candidates.add(int(num, 16))
            numbers = numbers[-1] + numbers[:-1]
                                                                 
        print(f"#{t+1}", end=" ")        
        print(sorted(candidates, reverse=True)[K-1])
        
solve()