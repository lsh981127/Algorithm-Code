import sys
input = sys.stdin.readline

goal = int(input())
current = 100
count = abs(100 - goal) # 처음부터 1로만 위 아래 처리할때 값을 기본
numset = set()
num = int(input()) # 사용 불가 갯수

if num != 0:
    numset = set(map(str, input().split()))
    # str로 읽어서 set의 key로 설정
else:
    numset = set()

if goal == 100:
    print(0)
    exit(0)

for i in range(1000001): # goal * 2 +1
    current_set = str(i)
    if len(numset & set(current_set)) != 0: # 사용 불가숫자랑 곂치는 게 있으면
        continue
    else:
        count = min(count, abs(goal - i) + len(str(i)))
        # abs(goal - i) : 목표값이랑 1씩 증감 count 수
        # len(i) : i 길이만큼 눌러줘야하는 숫자 횟수

print(count)
    