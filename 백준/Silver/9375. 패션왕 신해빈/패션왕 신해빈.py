import sys
from itertools import combinations
input = sys.stdin.readline

tcase = int(input())
for _ in range(tcase):
    memo = dict()
    count = int(input())
    total = 1
    if count == 0:
        print(0)
    else:
        for _ in range(count):
            name, type = input().split()
            
            if type in memo:
                memo[type] += 1
            else:
                memo[type] = 1
        
        for k in memo: # 키만 출력
            total *= (memo[k] + 1)
            
        
        print(total - 1)