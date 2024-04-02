import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    li = list(map(int, list(input().rstrip())))
    # 문자열을 리스트로 만들어서 나눠주고, 각 자료형을 int로 바꿔준 뒤 다시 list로 만들기
    arr.append(li)
    # int 값으로 인접 배열로 만들기

# 최단 경로는 BFS로 진행
queue = deque()
queue.append((0,0))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 최대한 우, 아래로 가야하는데

# (N-1,M-1)이 목표
# 튜플안에 좌표값으로 위치 이동

# BFS 방식
# 최소의 기준을 어떻게 처리할지 모르겠네

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1 # 방문 처리
    
print(arr[N-1][M-1])
# count로 하려니 그냥 모든 너비의 갯수가 count가 되기에 최단 거리로 정이할 수 있는 방법이 없었음

