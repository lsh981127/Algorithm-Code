import sys
input = sys.stdin.readline

r, c = map(int,input().split())

graph = [list(map(str, input().rstrip())) for _ in range(r)]
# split하면 안나눠진다... 띄어쓰기 있는 줄 알았다...
# rstrip으로 해야합니다..

direction = [(-1, -1), (-1, 0), (-1, 1)]  # 가능한 y 좌표가 작은 위치로 하는 게 좋지
count = 0

def dfs(x, y):
    global count
    if x == 0:
        count += 1
        return True
    
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx and 0 <= ny and ny < r and graph[ny][nx] == ".":
            graph[ny][nx] = 'x'
            if dfs(nx, ny):
                return True
    return False

for y in range(r):
    dfs(c-1, y)
    
print(count)