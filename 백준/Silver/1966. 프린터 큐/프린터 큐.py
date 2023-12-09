import sys
from collections import deque

input = sys.stdin.readline

def print_queue(num, queue):
    # num : 출력해야하는 값의 index
    # queue[][0]
    # 연산다하고 결과 result에 append
    # 내부 튜플 0 : 처음 index, 1: 중요도
    count = 0
    temp = queue
    max_prio = max(temp, key = lambda x: x[1])[1]
    while True:
        if temp[0][1] == max_prio:
            # 최대 중요도랑 같을떄
            if num == temp[0][0]: # 지금 들어온 게 목표한 index일떄
                count += 1
                result.append(count)
                break
            count += 1
            temp.popleft()
            max_prio = max(temp, key = lambda x: x[1])[1]
            
        else:
            temp.append(temp.popleft())
    
    
test_case = int(input())
result = []

for i in range(test_case):  
    doc_num, doc_index = map(int, input().split())
    testcase_list = deque(map(int, input().split()))
    testcase_list = deque([(idx, d) for idx, d in enumerate(testcase_list)])
    # 튜플로 저장하면 찾아야하는 index 값이 안변하니 편함
    print_queue(doc_index, testcase_list)
    
for i in result:
    print(i)