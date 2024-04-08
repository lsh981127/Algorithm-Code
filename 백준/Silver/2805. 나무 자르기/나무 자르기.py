import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # 정렬
start, end = 0, arr[-1] # 최소 길이 0, 최대 길이: 리스트의 마지막값
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid
            
    if total < M:
        end = mid -1
    else:
        start = mid + 1

print(end)
    