import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 인접 행렬

virus = deque()  # 바이러스 숙주 원 위치
wall_avail = deque()  # 벽 둘 수 있는 곳, 즉 0 위치들
for i in range(n):  # 맨 처음 virus 위치값 더하기
    for j in range(m): 
        if arr[i][j] == 1:  # 벽 갯수 count
            continue
        elif arr[i][j] == 0:  # 빈 공간
            wall_avail.append((i,j))
        elif arr[i][j] == 2:  # 바이러스 숙주
            virus.append((i,j))

wall_num = n*m - len(wall_avail) - len(virus) + 3 # 마지막 3은 앞으로 지을 벽 갯수 추가한 것
max_val = 0
dx = [1, -1, 0, 0]  
dy = [0, 0, 1, -1]

for zero_rand in combinations(wall_avail, 3):
    # 3군데에 연구소 값인 1로 설정
    for x, y in zero_rand:
        arr[x][y] = 1
    
    # bfs 시작(각 숙주 바이러스들을 이미 visited 했다고는 하고 queue에 넣어둬서 진행하면 문제 없음)
    visited = [[0]*m for _ in range(n)]
    queue = deque(virus)
    total_virus = len(virus)  # 전체 바이러스 갯수 세는 변수
    for x, y in virus:
        visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if 0 <= rx < n and 0 <= ry < m:
                if visited[rx][ry] == 0 and arr[rx][ry] == 0:  # 방문 안한 연구소인 경우
                    visited[rx][ry] = 1
                    queue.append((rx,ry))
                    # 감염 시킨 것
                    total_virus += 1
    
    max_val = max(max_val, n * m - wall_num - total_virus)
    for x, y in zero_rand:
        arr[x][y] = 0
        
print(max_val)