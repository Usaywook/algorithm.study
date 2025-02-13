import heapq
    
class Shark:
    def __init__(self, pos_i, pos_j):         
        self.pos = (pos_i, pos_j)
        self.size = 2
        self.eat_count = 0
        self.move_count = 0
            
    def __repr__(self):
        return f"pos: {self.pos}, size: {self.size}, eat_count: {self.eat_count}, move_count: {self.move_count}"          

class Solver:
    def __init__(self, N, maze):
        self.N = N
        self.maze = maze        
        
        self.di = [1, -1, 0, 0]
        self.dj = [0, 0, -1, 1]
        for i in range(N):
            for j in range(N):
                key = self.maze[i][j]
                if key == 9:
                    self.shark = Shark(i,j)
    
    def getTarget(self):    
        visited = [[False] * self.N for _ in range(self.N)]
        visited[self.shark.pos[0]][self.shark.pos[1]] = True
        queue = []
        queue.append((0, self.shark.pos[0], self.shark.pos[1]))
        
        min_dist = 1000
        candidates = []
        while queue:
            dist, pos_i, pos_j = heapq.heappop(queue)
            
            if dist > min_dist: continue
            
            for k in range(4):        
                next_i = pos_i + self.di[k]
                next_j = pos_j + self.dj[k]                                  
                if next_i < 0 or next_i > self.N - 1 or next_j < 0 or next_j > N - 1: continue     
                if visited[next_i][next_j]: continue
                            
                fish_size = self.maze[next_i][next_j]  
                if fish_size > self.shark.size: continue
                             
                visited[next_i][next_j] = True
                next_dist = dist + 1
                if fish_size != 0 and fish_size != self.shark.size:
                    min_dist = next_dist
                    candidates.append((min_dist, next_i, next_j))

                heapq.heappush(queue, (next_dist, next_i, next_j))                
        
        if candidates:
            candidates.sort(key=lambda x: (x[0], x[1], x[2]))
            target = candidates[0]
            return (target[1],target[2]), target[0]
        else:
            return None, 0 
    
    def solve(self):
        while True:
            target, dist = self.getTarget()
            if not target:
                break

            self.maze[self.shark.pos[0]][self.shark.pos[1]] = 0            
            self.shark.pos = target
            self.maze[target[0]][target[1]] = 9
            self.shark.move_count += dist                   
            
            self.shark.eat_count += 1
            if self.shark.eat_count >= self.shark.size:
                self.shark.size += 1
                self.shark.eat_count = 0
            
        return self.shark.move_count
    
if __name__ == "__main__":
    import sys
    sys.stdin = open("baby_shark.txt",'r')
    T = int(input())    
    for t in range(T):        
        print(f"#{t}", end=" ")
        N = int(input())     
        maze = []
        for _ in range(N):
            maze.append(list(map(int, input().split())))

        solver = Solver(N, maze)
        ans = solver.solve()
        print(ans)    
        