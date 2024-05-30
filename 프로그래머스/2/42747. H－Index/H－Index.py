def solution(citations):
    answer = 0
    index = 0
    arr = sorted(citations, reverse=True)
    for i in range(len(arr)):
        if arr[i] < i+1:
            # H index 존재
            answer = i  # 인덱스를 넣어주잖아
            return answer
    return len(citations)