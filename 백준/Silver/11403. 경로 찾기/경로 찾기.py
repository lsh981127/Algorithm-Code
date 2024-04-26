import sys
input = sys.stdin.readline

N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if path[i][k] and path[k][j]: # 둘 중 하나라도 1이 있으면 경로가 있다는 것이니
                path[i][j] = 1

for i in path:
    print(*i)