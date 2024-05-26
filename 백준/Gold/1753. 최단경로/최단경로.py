import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
arr = [[] for i in range(V+1)]
start = int(input())
INF = 10e9
distance = [INF]*(V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v,w)) # u에서 v로 간선 w
    

# start 노드부터 다른 노드까지의 최단 거리만 구면 돼 = 다익스트라
def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijk(start)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
