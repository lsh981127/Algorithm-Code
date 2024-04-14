import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))


dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                queue.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1

result = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()  
    result = max(result, max(i))

print(result-1)