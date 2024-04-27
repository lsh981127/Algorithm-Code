import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
parsum = [0]
temp = 0
for i in arr:
    temp += i
    parsum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    i = i - 1
    j = j - 1
    print(parsum[j+1] - parsum[i])