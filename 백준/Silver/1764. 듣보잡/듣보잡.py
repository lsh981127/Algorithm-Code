import sys
input = sys.stdin.readline

N, M = map(int, input().split())
total = sys.stdin.read().splitlines()

listen = set(total[:N])  # N개까지 listen을 바로 읽어버리네
seen = set(total[N:])
total = list(listen & seen) # set간 &로 교집합 처리하면 겹치는 걸 바로 찾기
total.sort()

print(len(total))
for i in total:
	print(i)