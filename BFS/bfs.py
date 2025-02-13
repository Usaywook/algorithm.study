import collections

def bfs(Graph, start_node, visited=set()):
    visited.add(start_node)
    Queue = collections.deque([start_node])
        
    while Queue:
        node = Queue.popleft()
        print(node)
        
        for neighbor in Graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                Queue.append(neighbor)
    
Graph = {
    0: set([1,3]),
    1: set([0,2,4]),
    2: set([0,1,4]),
    3: set([0]),
    4: set([2]),
}

bfs(Graph, 0)