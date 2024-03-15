
# def solution(participant, completion):
#     answer = set(participant) - set(completion)
#     return answer.pop()

# 동명이인이 있네;;
# 이러면 set 쓰면 안된다
def solution(participant, completion):
    part = {}
    total = 0
    for i in participant:
        part[hash(i)] = i
        total += hash(i)
    
    for j in completion:
        total -= hash(j)
    
    # total은 그냥 int 값
    return part[total]