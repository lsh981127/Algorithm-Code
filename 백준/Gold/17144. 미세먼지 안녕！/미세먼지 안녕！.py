import sys

# input = sys.stdin.readline
r, c, t = map(int, sys.stdin.readline().split())

dust = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

cur = []
cleaner = []

def bfs():
    while cur:  # 실제 먼지가 들어가 있는 부분이 처리될 때 까지
        x, y, value = cur.pop()
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny <0 or ny >= c:
                continue
            
            if (nx, ny) in cleaner:
                continue
            
            dust[nx][ny] += value//5
            count += 1
        dust[x][y] -= (value//5) * count        

def clean(a,b):
    x, y = a, 1 # y가 1인 이유는 공기청정기가 0행에 있어서 1행부터 시작하도록
    index = 1 
    temp = 0  # 맨 처음에 공기청정기에서 나오는 값 및 임시 값 저장용 변수
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == r or ny == c or nx == -1 or ny == -1:
            index = (index - 1) % 4 # 나머지 기준으로 생각하면 우, 하, 좌, 상 순서로 움직이게 됨
            continue
        if x == a and y == 0: # 공기청정기 머리
            break
        
        dust[x][y], temp = temp, dust[x][y]
        x, y = nx, ny
    
    x, y = b, 1
    index = 1
    temp = 0
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == r or ny == c or nx == -1 or ny == -1:
            index = (index + 1) % 4
            continue
        if x == b and y == 0:
            break
        dust[x][y], temp = temp, dust[x][y]
        x, y = nx, ny
        

for i, column in enumerate(dust): # 열과 행
    for j, value in enumerate(column): # 행의 index과 값
        if value > 0:
            cur.append((i, j, value))
        if value == -1:
            cleaner.append((i,j))
        
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

head = cleaner[0][0]
tail = cleaner[1][0]        

for _ in range(t):
    bfs()
    clean(head, tail)
    # 다 돌리면 cur 다시 초기화
    for i, column in enumerate(dust):
        for j, value in enumerate(column):
            if value>0:
                cur.append((i,j,value))
print(sum(cur[i][2] for i in range(len(cur))))
