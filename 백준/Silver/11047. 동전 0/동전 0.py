import sys

input = sys.stdin.readline
N, K = map(int, input().split())
goal = K
coin = []
count = 0
for _ in range(N):
    coin.append(int(input()))
    
for i in range(N, 0, -1):
    if coin[i-1] > goal:
        continue
    
    count += goal // coin[i-1]
    goal = goal % coin[i-1]
    
    if goal == 0:
        print(count)