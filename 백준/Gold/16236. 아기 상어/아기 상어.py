import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

start_x, start_y = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 2
time = 0
eat_count = 0
for i in range(n):
    if 9 not in graph[i]:
        continue
    else:
        start_x = i
        start_y = graph[i].index(9)


def bfs(x, y, shark_size):
    queue = deque() # 이동 경로용 큐
    distance = [[0]*n for _ in range(n)]  # 먹이들 거리
    visited = [[0]*n for _ in range(n)]  # 방문
    queue.append((x,y))
    visited[x][y] = 1
    eat = []
    while queue:
        tmp_x, tmp_y = queue.popleft()
        
        for i in range(4):  #  4가지 방향
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size: # 상어 크기보다 같거나 작아 => 이동 가능
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[tmp_x][tmp_y] + 1 # 기존것보다 1칸 이동
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:  # 먹을 수 있는 것
                        eat.append((nx,ny,distance[nx][ny]))
    return sorted(eat, key=lambda x: (-x[2], -x[0], -x[1]))  # 가장 가깝고, 왼쪽, 위에 있는 걸 지우기 위해 앞으로 오도록 정렬       

while 1:
    shark = bfs(start_x, start_y, size)
    if len(shark) == 0:
        break
    
    nx, ny, dist = shark.pop()
    time += dist
    graph[start_x][start_y], graph[nx][ny] = 0, 0 # 초기화
    start_x, start_y = nx, ny  # 먹은 물고기 위치로 상어 이동
    eat_count += 1
    if eat_count == size:   # 먹은 물고기수 = 상어 크기
        eat_count = 0
        size += 1
        
        
print(time)