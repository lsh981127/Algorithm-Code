import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    dx = [1, 0, -1, 0] # 하 좌 상 우
    dy = [0, -1, 0, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                dfs(nx,ny)

for _ in range(int(input())):
    m, n, num = map(int, input().split())  # m : 가로, n : 세로
    arr = [[0 for _ in range(m)] for _ in range(n)]  # 인접 행렬
    result = 0
    
    for _ in range(num):
        y, x = map(int, input().split())  # input 값으로 가로 index, 세로 index 들어와서 순서 바꿔줌
        
        arr[x][y] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(i,j)
                result +=1
    print(result)
