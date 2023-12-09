import sys

input = sys.stdin.readline

equation = list(map(str, input().split('-')))

total = 0
for i,d in enumerate(equation):
    plusnum = list(map(int, d.split('+')))  # 숫자들 리스트 
    if i == 0:
        total += sum(plusnum)   # 안에 있는 숫자 전부 더하기
        continue
    
    total -= sum(plusnum)
    
print(f'{total}')