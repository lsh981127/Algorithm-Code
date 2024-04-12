import sys
from collections import deque

input = sys.stdin.readline


M, N, H = map(int, input().split())

arr = []
for _ in range(H):
    arr.append([list(map(int, input().split())) for _ in range(N)]) 


dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
queue = deque()
def bfs():
    while queue:
        c,a,b = queue.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[c][a][b] + 1
                    queue.append((nz,nx,ny))



for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                queue.append((k,i,j))  # 제일 처음에 1인 값들만 넣어두기

bfs()

result = 0
for k in arr:
    for x in k:
        for y in x:
            if y == 0:
                print(-1)
                exit()
        result = max(result, max(x))            
print(result-1)
            
            
