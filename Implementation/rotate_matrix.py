def rotateClockwise(array):    
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = array[N - j - 1][i]
    return tmp

def transpose(array):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):            
            tmp[i][j] = array[j][i]
    return tmp

def rotateCounterClockwise(array):    
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = array[j][N - i - 1]
    return tmp
            
def printArray(array):    
    print('[', end='')
    for i in range(N):
        if i == 0:
            print('[', end=' ')
        else:
            print(' [', end=' ')
        for j in range(N):
            print(array[i][j], end=' ')
        if i == N-1:
            end = ''
        else:
            end = '\n'
        print(']', end=end)        
    print(']')
    
array = [[1,2,3],[4,5,6],[7,8,9]]
N = len(array)

printArray(array)
printArray(transpose(array))
printArray(rotateClockwise(array))
printArray(rotateCounterClockwise(array))