import sys
input = sys.stdin.readline

card_own = int(input())  # 보유 카드 수

# 보유한 카드에 적힌 숫자 / 해당 숫자의 갯수 이렇게만 저장하면 돼
# 이건 dict 형태로 저장? map 형태로 저장
# 임시 list 형태 read
card_own_dict = list(map(int, input().split()))
a = dict()
for i, data in enumerate(card_own_dict):
    if data not in a:
        a[data] = 1
        continue
    a[data] += 1
    
card_find = int(input())  # 찾을 카드 수
card_findlist = list(map(int, input().split()))

result = [0] * card_find
for i, d in enumerate(card_findlist):
    # 찾을 숫자들을 key로 넣어서 value 값을 그대로 저장하기
    if d in a:
        result[i] = a[d]
    
print(*result)