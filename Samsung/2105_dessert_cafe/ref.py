import sys
sys.stdin = open("input.txt", "r")
sys.path.append('../../')
from evaluator import memory_usage_decorator

# 대각선
# 왼쪽 아래 
# 오른쪽 아래 
# 오른쪽 위 
# 왼쪽 위 
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

def find_path():
    for total_length in range(N - 1, 1, -1):
        for l1 in range(1, total_length):
            l2 = total_length - l1
            for sr in range(N - l1 - l2):
                for sc in range(l1, N - l2):
                    v = [0] * 101
                    r, c = sr, sc
                    for d in range(4):
                        l = l2 if d % 2 else l1
                        for _ in range(l):
                            r += dr[d]
                            c += dc[d]
                            if not v[MAP[r][c]]:
                                v[MAP[r][c]] = 1
                            else:
                                break
                        else:
                            continue
                        break
                    else:
                        return total_length * 2
    return -1

@memory_usage_decorator
def main():
    global T, N, MAP
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = find_path()
        print(f"#{tc} {ans}")

main()
