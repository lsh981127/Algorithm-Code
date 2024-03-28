import sys
from collections import deque

input = sys.stdin.readline

start, end = map(int, input().split())
# 최대를 그냥 혹시 모르니 start, end 중 큰 숫자의 2배 + 1까지만 설정
maxval = int(10e5)
visited = [0] * (maxval+1)

queue = deque()
queue.append(start)
while queue:
    index = queue.popleft()
    if index == end:
        break
    for j in (index -1, index + 1, index * 2): # index -1, index + 1, index * 2 순서
        if 0 <= j < maxval and visited[j] == 0: # not visited[j], 
            queue.append(j)
            visited[j] = visited[index] + 1

print(visited[end])
    
        