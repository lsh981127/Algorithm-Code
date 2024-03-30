import sys
import heapq

input = sys.stdin.readline

N = int(input())
result = []

for i in range(N):
    temp = int(input())
    if temp != 0:
        heapq.heappush(result, temp)
    else:
        if not result: # 리스트 비어있으면
            print(0)
            continue
        print(heapq.heappop(result))