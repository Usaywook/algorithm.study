import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1,T+1):
    K = int(input())
        
    array = []
    for _ in range(4):
        array.append(list(map(int, input().split())))
    
    rotates = []
    for _ in range(K):
        rotates.append(tuple(map(int, input().split())))
        
    def direction(k, d):
        # 뒤쪽
        dirs = {k-1 : d}    
        bd = d    
        for i in range(k, 4):
            if array[i-1][2] == array[i][-2]:
                break                                
            else:
                bd = -bd
                dirs[i] = bd            
            
        # 앞쪽    
        fd = d    
        for i in range(k-1, 0, -1):
            if array[i][-2] == array[i-1][2]:                
                break                      
            else:
                fd = -fd
                dirs[i-1] = fd                        
        return dirs    
    
    def rotate(magnet, d):
        if d == 1:
            return [magnet[-1]] + magnet[:-1]                                    
        elif d == -1:
            return magnet[1:] + [magnet[0]]       
        elif d == 0:
            return magnet 
        else:
            print(f"direction is not defined {d}")
            raise NotImplementedError
        
    def count():                
        return sum([array[k][0]*2**k for k in range(4)])
        
    for (num, dir) in rotates:
        turns = direction(num, dir)          
        for k, d, in turns.items():
            array[k] = rotate(array[k], d)                
    ans = count()        
            
    print(f"#{t} {ans}")    