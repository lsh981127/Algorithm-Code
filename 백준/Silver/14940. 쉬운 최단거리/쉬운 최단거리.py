import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x, y = 0, 0

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] != 2:
            continue
        else:
            x = i
            y = j
            
graph[x][y] = 0
visited[x][y] = 1
queue = deque()
queue.append((x,y,0))
dir = [(1,0),(0,1),(-1,0),(0, -1)]

while queue:
    a,b,count = queue.popleft()
    for dx, dy in dir:
        nx = a + dx
        ny = b + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                graph[nx][ny] = max(graph[nx][ny], count + 1) 
                visited[nx][ny] = 1
                queue.append((nx,ny, count + 1))
                
                
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in graph:
    print(*i)

