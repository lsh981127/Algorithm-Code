import heapq, sys
input = sys.stdin.readline

num = int(input())
arr = []
for _ in range(num):
    temp = int(input())
    if temp == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr) * (-1))
    else:
        heapq.heappush(arr, temp * (-1))

