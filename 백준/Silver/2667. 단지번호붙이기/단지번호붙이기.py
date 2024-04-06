import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
result = []

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    count = 0
    while queue:
        x, y = queue.popleft()
        if arr[x][y] != 1:
            continue
        count += 1
        arr[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                queue.append((nx,ny))
    return count

for i in range(N):
    for j in range(N):
        if arr[i][j] != 1:
            continue
        result.append(bfs(i, j))
            
result.sort()
print(len(result))
for i in result:
    print(i)