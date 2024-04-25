import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()
total = 0
for i in range(N):
    temp = arr[i] * (N-i)
    total += arr[i] * (N-i)
    
print(total)