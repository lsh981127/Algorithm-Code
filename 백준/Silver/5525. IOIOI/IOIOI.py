import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input() # 리스트 안만들고 그냥 이렇게 해서 문자열로 분할하는 거였네

i = 0
count = 0
result = 0

while i < (M-1):
    if S[i:i+3] == "IOI":
        i+=2
        count += 1
        if count == N:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)