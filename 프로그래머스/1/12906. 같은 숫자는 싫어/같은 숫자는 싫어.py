def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    cur = -1
    for i, val in enumerate(arr):
        if cur != val:
            answer.append(val)
        cur = val
        
    return answer