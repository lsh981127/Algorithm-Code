def solution(array, commands):
    answer = []
    for arr in commands:
        i, j, num = arr[0]-1, arr[1]-1, arr[2]-1
        # index 용으로 변환
        test = sorted(array[i:j+1])
        answer.append(test[num])
        
        
    return answer