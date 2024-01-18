import heapq
import sys

input = sys.stdin.readline
Inf = int(1e9)

n, m, k, x = map(int,input().split())
result = []
# 각 노드에 연결되어 있는 노드들에 대한 리스트
# 인접 리스트 => 메모리 용량 덜 차지함
graph = [[] for i in range(n+1)]

visited = [False] * (n+1)
distance = [Inf]*(n+1)

for _ in range(m):
	a,b = map(int, input().split())
	graph[a].append((b,1))
	# 튜플로 연결된 노드, 가중치 형태로 저장


def dijkstra(start):
	q =[]
	# 시작노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
	heapq.heappush(q, (0,start))
	distance[start] = 0
	while q:
		# 가장 최단 거리가 짦은 노드 꺼내기
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in graph[now]:  # 현재 노드와 인접한 노드 확인
			cost = dist + i[1]
			if cost < distance[i[0]]: # 현재 노드 거쳐서 다른 노드로 이동하는 거리가 짧은 경우 확인
				distance[i[0]] = cost
				heapq.heappush(q, (cost,i[0]))



dijkstra(x)

for i in range(1, n+1):
	# 리스트에 특정 거리인 것들 append
	if distance[i] == k:
		result.append(i)

if len(result) != 0:
	result.sort()
	for i in result:
		print(i)
else:
	print(-1)
	# len == 0 이며 -1 return