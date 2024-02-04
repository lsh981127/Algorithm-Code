import sys
input = sys.stdin.readline

n = int(input()) 
arr = list(map(int, input().split()))
maxDP = arr
minDP = arr

maxDP = arr
minDP = arr
for _ in range(n - 1):
    arr = list(map(int, input().split()))
		# 매 행 실행할떄마다 기존 maxDP에 업데이트 하는 방식
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))