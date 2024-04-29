import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(node):
    for i in graph[node]:
        if not visited[i]: # 방문 안했으면
            visited[i] = 1
            dfs(i)
            
connected = 0
for i in range(len(graph)):
    if i == 0:
        continue
    if not visited[i]:
        dfs(i)
        connected += 1
            
print(connected)