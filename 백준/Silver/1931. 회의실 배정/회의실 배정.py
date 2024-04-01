import sys
input = sys.stdin.readline
N = int(input())

conf = []
for _ in range(N):
    start, end = map(int, input().split())
    temp = end - start
    conf.append((start, end))
    
# (시작, 끝, 길이)
# 시작 기준으로 sort 하고 난 뒤, 길이 짧은 것들부터 넣기?
sorted_conf = sorted(conf, key=lambda x: (x[1],x[0]))
# lambda x: (x[1], x[0]) 이란?
# x[1] 순으로 먼저 정렬한 뒤!, x[0] 순서로 정렬해라!

count = 0
endPoint = 0
for newStart, newEnd in sorted_conf:
    if endPoint <= newStart:
        count += 1
        endPoint = newEnd

print(count)