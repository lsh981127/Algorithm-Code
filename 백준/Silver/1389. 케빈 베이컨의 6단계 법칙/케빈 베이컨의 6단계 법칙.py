import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[1000 for _ in range(N)] for _ in range(N)]
result = []

for i in range(N):
    arr[i][i] = 0

for _ in range(M):
	a, b = map(int, input().split())
	arr[a-1][b-1] = 1
	arr[b-1][a-1] = 1

# 플로이드 와샬
for k in range(N):
	for i in range(N):
		for j in range(N):
			arr[i][j] = min(arr[i][j], arr[i][k]+ arr[k][j])
			
# print(arr)

for i in range(N):
	result.append(sum(arr[i])) # 각 사람 합값 넣기
	
print((result.index(min(result))) + 1)

			