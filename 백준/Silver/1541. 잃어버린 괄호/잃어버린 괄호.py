import sys

input = sys.stdin.readline

# 그리디 문제로 - 와 - 사이의 값들만 합치면 최솟값이 된다.
# 1. 그렇기에 식 자체를 읽을때부터 - 기준으로 파싱한 뒤
# 2. 나누어진 각각의 리스트들의 합을 구한고
# 제일 처음의 값을 제외한 나머지 값들은 빼는 방법으로 구현하면 된다.

equation = list(map(str, input().split('-')))

total = 0
for i,d in enumerate(equation):
    plusnum = list(map(int, d.split('+')))  # 숫자들 리스트 
    if i == 0:
        total += sum(plusnum)   # 안에 있는 숫자 전부 더하기
        continue
    
    total -= sum(plusnum)
    
print(f'{total}')
