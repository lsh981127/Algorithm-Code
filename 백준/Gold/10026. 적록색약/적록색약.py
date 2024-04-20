import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
visited = list([0]*n for _ in range(n))

color = [list(input().rstrip()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

case1, case2 = 0, 0

def dfs(x,y):
    visited[x][y] = 1
    col = color[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and color[nx][ny] == col:
                dfs(nx, ny)
                         
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            case1 += 1

for i in range(n):
    for j in range(n):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = list([0]*n for _ in range(n))
  
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            case2 += 1

print(case1, case2)