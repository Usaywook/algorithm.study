def dfsStack(Graph, node, visited=set()):
    visited.add(node)
    
    stack = [(node, visited)]
    while stack:
        node, visited = stack.pop()
        yield node
        
        for neighbor in Graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, visited))
        
def dfsTopDown(Graph, node, visited=set()):
    """
    탐색 및 처리를 방문 즉시 수행하는 방식
    """
    visited.add(node)
    # print(node)
    yield node
    
    for neighbor in Graph[node]:
        if neighbor not in visited:
            # dfsTopDown(Graph, neighbor, visited)
            yield from dfsTopDown(Graph, neighbor, visited)

def dfsBottomUp(Graph, node, visited=set()):
    """
    탐색을 먼저 마치고 결과를 모아서 처리하는 방식
    """
    # Base case: If the node is already visited, return an empty list
    if node in visited:
        return []

    visited.add(node)

    # Collect results from neighbors
    # result = []
    for neighbor in Graph[node]:
        # result.extend(dfsBottomUp(Graph, neighbor, visited))
        yield from dfsBottomUp(Graph, neighbor, visited)

    # Add the current node to the result
    # result.append(node)
    # return result
    yield node

Graph = {
    0: set([1,3]),
    1: set([0,2,4]),
    2: set([0,1,4]),
    3: set([0]),
    4: set([2]),
}

print("DFS stack:")
# dfsStack(Graph, 0)
for node in dfsStack(Graph, 0):
    print(node)
    
print("DFS Top Down:")
# dfsTopDown(Graph, 0)
for node in dfsTopDown(Graph, 0):
    print(node)

print("DFS Bottom Up:")
for node in dfsBottomUp(Graph, 0):
    print(node)