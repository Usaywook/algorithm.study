from itertools import permutations

def create_graph(array):
    """
    주어진 배열로부터 그래프를 생성합니다.
    각 노드는 배열의 요소를 나타내며, 모든 노드가 서로 연결된 완전 그래프를 만듭니다.
    """
    graph = {node: [n for n in array if n != node] for node in array}
    return graph

def dfs_all_paths(graph, start):
    """
    그래프의 모든 DFS 순회 경로를 계산합니다.
    """
    all_paths = []

    def dfs(path, visited):
        # 현재 노드를 path에 추가
        node = path[-1]
        if len(path) == len(graph):  # 모든 노드를 방문했다면
            all_paths.append(path[:])  # 현재 경로를 저장
            return

        # 현재 노드의 모든 이웃 탐색
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(path + [neighbor], visited)
                visited.remove(neighbor)

    def dfs_with_stack(start_node):
        stack = [(start_node, [start_node], set([start_node]))]

        while stack:
            current, path, visited = stack.pop()

            # print(current)
            # 모든 노드를 방문했다면 경로 저장
            if len(path) == len(graph):
                # print(path)
                all_paths.append(path)
                continue

            # 현재 노드의 모든 이웃 탐색
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], visited | {neighbor}))
                    
    # 그래프의 각 노드에서 시작하는 DFS 실행
    for start_node in graph.keys():
        # dfs([start_node], set([start_node]))
        dfs_with_stack(start_node)

    return all_paths

def traverse(array):
    all_paths = []
    N = len(array)
    
    print(f"start traverse!")
    for i in range(N):
        stack = [(array[i], {i}, [i])]
         
        while stack:
            curr, visited, path = stack.pop()            
            
            # visit node
            # print(f"visit {curr}")
            # print(f"already visited = {visited}")
            
            if len(visited) == N:
                # visit root
                print(f"visit root = {path}")
                all_paths.append([path])                
                continue
                
            # search neighbor
            for j in range(N):
                if j not in visited:
                    # print(f"visit neighbor = {path[-1]}")
                    next = array[j]
                    # check condition for neighbor to add stack
                    stack.append((next, visited | {j}, path + [j]))
                    
# 배열 정의 (예: N = 3)
N = 3
array = [f"Node{i}" for i in range(N)]

# # 그래프 생성
# graph = create_graph(array)

# # 모든 DFS 순회 경로 계산
# paths = dfs_all_paths(graph, start=array[0])

# # 결과 출력
# print("그래프:")
# for node, neighbors in graph.items():
#     print(f"{node}: {neighbors}")

# print("\n모든 DFS 순회 경로:")
# for path in paths:
#     print(" -> ".join(path))

traverse(array)