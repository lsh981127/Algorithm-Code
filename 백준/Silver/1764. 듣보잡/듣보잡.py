import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = {}
seen = {}
total = []
for i in range(N):
    listen[input().split()[0]] = 1


for j in range(M):
    seen[input().split()[0]] = 1
    

listen = dict(sorted(listen.items())) # 미리 sorted 하면 나중에 다시 추가할 필요 없음
seen = dict(sorted(seen.items()))
  
if min(N,M) == N:
    for i in listen.keys():
        if i in seen:
            total.append(i)
            
else:
    for i in seen.keys():
        if i in listen:
            total.append(i)
            
print(len(total))
for _, val in enumerate(total):
    print(val)
