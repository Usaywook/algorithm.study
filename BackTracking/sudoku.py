# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]

# shallow copy
# ans = board 

# build: 
# $env:Path += ";C:\Users\l7181\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts"
# pyinstaller --onefile --console sudoku.py
ans = []
print("아래처럼 9번 반복해서 각 행을 입력하고, 각 행을 입력한 뒤 Enter를 눌러주세요. 숫자와 빈칸(.)은 공백으로 구분합니다:")
print("""5 3 . . 7 . . . . (Enter)
6 . . 1 9 5 . . . (Enter)
. 9 8 . . . . 6 . (Enter)
8 . . . 6 . . . 3 (Enter)
4 . . 8 . 3 . . 1 (Enter)
7 . . . 2 . . . 6 (Enter)
. 6 . . . . 2 8 . (Enter)
. . . 4 1 9 . . 5 (Enter)
. . . . 8 . . 7 9 (Enter)
""")

for _ in range(9):
    ans.append(list(map(str, input().split())))
print("="*15 + "입력된 정보" + "="*15)    

for row in ans:                        
    print(row)

subBoxTable = {
    0: [(i,j) for j in range(3) for i in range(3)],
    1: [(i,j) for j in range(3,6) for i in range(3)],
    2: [(i,j) for j in range(6,9) for i in range(3)],
    3: [(i,j) for j in range(3) for i in range(3,6)],
    4: [(i,j) for j in range(3,6) for i in range(3,6)],
    5: [(i,j) for j in range(6,9) for i in range(3,6)],
    6: [(i,j) for j in range(3) for i in range(6,9)],
    7: [(i,j) for j in range(3,6) for i in range(6,9)],
    8: [(i,j) for j in range(6,9) for i in range(6,9)],
}

def getNextEmpty():    
    for i in range(9):
        for j in range(9):
            if ans[i][j] == '.':
                return (i,j)
    return None

def getSubBoxIdx(pos):
    i = pos[0] // 3
    j = pos[1] // 3
    subIdx = 3*i + j
    return subIdx

def getCandidate(pos):
    cand = set(map(str, range(1,10)))    
    # check row        
    cand -= set(ans[pos[0]])    
    # check col    
    cand -= set([ans[r][pos[1]] for r in range(9)])    
    # check sub-box
    idx = getSubBoxIdx(pos)
    cand -= set([ans[box[0]][box[1]] for box in subBoxTable[idx]])    
    return cand

def btRecur(pos, val):
    # process
    ans[pos[0]][pos[1]] = val   
    next_pos = getNextEmpty()
    
    # positive exit -> solved
    if next_pos is None:
        return True
    
    # call     
    for e in getCandidate(next_pos):    
        if btRecur(next_pos, e):    
            return True
    # rollback 
    ans[pos[0]][pos[1]] = '.'
    return False

def solve():
    pos = getNextEmpty()        
    for e in getCandidate(pos):
        if btRecur(pos, e):
            return True
    return False

if solve():
    print("스도쿠 해결!")
else:
    print("잘못된 입력을 주었습니다.")
    
print("="*15 + "결과" + "="*15)
for row in ans:                        
    print(row)
input("Press Enter to exit...")