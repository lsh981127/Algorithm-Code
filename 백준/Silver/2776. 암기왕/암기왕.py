import sys

input = sys.stdin.readline
test_case = int(input())

# 수첩 1 : 하루동안 본 정수들 다 본거
# M개 질문 던짐
# 수첩 2: 본 거 주장한 수
# 수첩 2에 적힌 순서대로 각 수에 수첩 1에 없으면 0, 있으면 1

for _ in range(test_case):
        # note 2의 값 순서대로 note 1 검색
        note1_num = int(input())
        note_1 = set(list(map(int, input().split())))

        note2_num = int(input())
        note_2 = list(map(int, input().split()))  # 원본
        for i in note_2:  # dict 초기화
            if i in note_1:
                print(1)
            else:
                print(0)