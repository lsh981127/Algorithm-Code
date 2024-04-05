import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 2중 배열 만들어주고
white, blue = 0, 0

def recur(n, x, y):
    global white, blue
    len = n // 2
    cur = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if cur != arr[i][j]: # 도중에 1개라도 틀리면
                recur(len, x, y)
                recur(len, x, y + len)
                recur(len, x+ len, y)
                recur(len, x+len, y+len)
                return
            
    if cur == 0:
        white += 1
    else:
        blue += 1

recur(N, 0, 0)
print(white)
print(blue)