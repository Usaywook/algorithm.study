import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))

    nodes = []
    for i in range(N+2):
        nodes.append(array[slice(2*i, 2*(i+1))])

    def getDist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def search(cur_ind, dist = 0, visited = set()):
        global ans
        if dist > ans:
            return

        cur_node = nodes[cur_ind]
        visited.add(cur_ind)

        if len(visited) > N:            
            ans = min(ans, dist + getDist(cur_node, nodes[1]))
            return

        for next_ind in range(2, N+2):
            next_node = nodes[next_ind]
            if next_ind not in visited:
                search(next_ind, dist + getDist(cur_node, next_node), visited | {next_ind})

    ans = 200 * N + 1
    search(0, visited={0})
    print(f"#{t} {ans}")


