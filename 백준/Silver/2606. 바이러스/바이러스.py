import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

M = int(input())
infected = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(n):
    global infected
    visited[n] = 1
    for i in graph[n]:
        if visited[i] != 1:
            infected += 1
            dfs(i)
    
dfs(1)
print(infected)