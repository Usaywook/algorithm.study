import sys

sys.stdin = open("input.txt", "r")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    
    cur_atoms = []
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        cur_atoms.append((x, y, d, e))        
    
    def move_atoms(atoms):        
        occupied = set()
        collide = set()
        for x, y, d, _ in atoms:
            x += 0.5 * dx[d]
            y += 0.5 * dy[d]
            if x < -1000 or x > 1000 or y < -1000 or y > 1000:
                continue
            if (x, y) in occupied:
                collide.add((x, y))
            else:                
                occupied.add((x, y))        
        
        new_atoms = []
        total_e = 0
        for x, y, d, e in atoms:
            x += 0.5 * dx[d]
            y += 0.5 * dy[d]
            if x < -1000 or x > 1000 or y < -1000 or y > 1000:
                continue
            if (x, y) in collide:
                total_e += e
                continue
            new_atoms.append((x, y, d, e))
                
        return new_atoms, total_e
    
    energy = 0
    for t in range(4000):
        cur_atoms, emission = move_atoms(cur_atoms) 
        # print(cur_atoms)
        energy += emission
        # print(f"After {(t+1)*0.5} s, Emissioned Energy : {energy}"
            
    print(f"#{test_case} {energy}")    
    
    