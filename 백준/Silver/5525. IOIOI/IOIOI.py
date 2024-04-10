import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().strip())
arr = ['O'] * N

P = list('I'+ 'I'.join(arr)+ 'I') # 1 ~ 01010 ~ 1

length = 2*N + 1
cursor = 0
result = 0
# print(P)
# print(S)
while cursor + length <= M:
    temp = S[cursor: cursor + length]
    if temp == P:
        result += 1
    
    cursor += 1

print(result)