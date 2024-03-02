import sys

input = sys.stdin.readline

num = int(input())

arr = list(map(int, input().split()))

lis = [arr[0]]

def bs(target):
    start, end = 0, len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == lis[mid]:  # 값 찾으면
            return mid
        elif lis[mid] > target: # mid 값이 더 크면
            end = mid -1
        else: # mid 값이 target 보다 작은 경우
            start = mid + 1
    return start

for i in range(1,num):
    tar = arr[i]
    if arr[i] > lis[-1]:   # 부분수열 제일 큰 값보다 크면
        lis.append(arr[i])
    else:
        idx = bs(tar)
        lis[idx] = tar

print(len(lis))
