import sys
input = sys.stdin.readline

INF = int(1e9)

# v: 노드 갯수, e : 간선 갯수
v, e = map(int, input().split())

# 모든 간선 리스트(인접 리스트)
edges = []

# 최단 거리 테이블 초기화(노드 번호에 맞춰서 index 세팅하기 떄문에 노드갯수 + 1의 index 생성)
distance = [INF] * (v+1)

# 모든 간선 정보 튜플 형태로 입력
for _ in range(e):
	sv, ev, cost = map(int, input().split())
	edges.append((sv,ev,cost))

# 벨만-포드 알고리즘
def bellmanFord(start):
	# 시작 노드 초기화
	distance[start] = 0
	
	# v번 edge relaxation을 반복
	# v-1번 탐색 + 마지막 1번은 음수 순환 사이클 검사
	for i in range(v):
		for j in range(e):
			current, next, edgeCost = edges[j]
			if distance[current] != INF and distance[current] + edgeCost < distance[next]:
				distance[next] = distance[current] + edgeCost
				if i == v - 1:  # v 번째 반복에서 갱신되는 값이 있으면 negative cycle이 존재하니 v-1번쨰에서 그냥 알고리즘 끝내버림
					return False
	# 정상 종료시
	return True


if bellmanFord(1):
	# 정상적으로 끝난 경우
	for i in range(2, v+1):
		if distance[i] == INF:
			print("-1")
		else:
			print(distance[i])
else:
	print("-1")
	
