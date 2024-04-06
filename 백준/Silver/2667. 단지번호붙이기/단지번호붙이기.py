from collections import deque

N = int(input())
houses = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(q):
    cnt = 0
    while(q):
        x,y = q.popleft()

        if visited[x][y]:
            continue
        cnt += 1
        visited[x][y] = 1
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < N and houses[nx][ny] == '1' and not visited[nx][ny]:
                q.append((nx,ny))
    return cnt

building = []
for i in range(N):
    for j in range(N):
        if houses[i][j] =='0' or visited[i][j]:
            continue

        cnt = bfs(deque([(i,j)]))
        building.append(cnt)

building.sort()
print(len(building))
for i in building:
    print(i)