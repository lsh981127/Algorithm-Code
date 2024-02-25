import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

glacier = [list(map(int, input().split())) for _ in range(n)]
ice = []
for i in range(n):
	for j in range(m):
		if glacier[i][j]:
			ice.append((i,j))


# BFS로 인접 확인하면서 동서남북 check
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y): # x : 열, y : 행
	queue = deque([(x,y)])   # 튜플로 좌표값을 저장
	melt_list = []
	visited[x][y] = 1
	while queue:
		temp_x, temp_y = queue.popleft()
		zero_count = 0
		for i in range(4):
			nx = temp_x + dx[i]
			ny = temp_y + dy[i]
			# 오, 왼, 밑, 위 순서
			if 0 <= nx < n and 0 <= ny < m:
				if glacier[nx][ny] == 0:  # 주위 값 0이면 녹이는 거 1 추가
					zero_count += 1
					continue
				elif visited[nx][ny] == 0: # 주위값 0 아니면
					queue.append((nx,ny))
					visited[nx][ny] = 1
		# 동서남북 확인하고 녹여야할 값을 저장
		if zero_count > 0:
			melt_list.append((temp_x, temp_y, zero_count))
	# 큐 끝나고
	for x, y, num in melt_list:
		glacier[x][y] = max(0, glacier[x][y] - num)  # 값 빼고 0이랑 max로 알아서 값 처리
	return 1

year_count = 0

while ice: 
	visited = [[0 for _ in range(m)] for _ in range(n)]
	group = 0
	melted_list = []
	for i, j in ice:
		if glacier[i][j] and not visited[i][j]: # 값 0 아니고 방문 안했음
			group += bfs(i, j)
		if glacier[i][j] == 0:  # bfs를 돌리고 다 녹아버리면 ice 리스트에서 제거할 용도
			melted_list.append((i,j))
	if group > 1:
		print(year_count)
		break
	ice = list(set(ice) - set(melted_list))  # set를 활용해 차집합, 중복되는 거 다 제가
	year_count += 1

if group < 2:
	print(0)