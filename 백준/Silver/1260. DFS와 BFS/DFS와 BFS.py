import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # N+1개 해서 노드 수 1부터 시작하도록
visited = [0] * (N+1)

dfs_list = []
bfs_list = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 반대 노드도 넣어줘야해!!, 간선의 방향이 있는 문제가 아니기에!!

for i in range(N+1):
    graph[i].sort()

# print(graph)

def dfs(start):
    visited[start] = 1
    dfs_list.append(start)
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
    
    
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        bfs_list.append(node)
        visited[node] = 1
        for val in graph[node]:
            if visited[val] == 0: # 연결된 노드를 안했으면
                visited[val] = 1
                queue.append(val)
                    

# 출력
dfs(V)
visited = [0] * (N+1) # dfs 돌리고 visited 다시 초기화
bfs(V)
print(*dfs_list)
print(*bfs_list)
