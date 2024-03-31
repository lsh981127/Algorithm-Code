from collections import deque
def solution(queue1, queue2):
    one = deque(queue1)
    two = deque(queue2)
    
    onesum = sum(queue1)
    twosum = sum(queue2)
    
    if (onesum + twosum) % 2 != 0:  # 합이 짝수여야 둘의 길이가 같아지니
        return -1
    
    goal = (onesum + twosum) // 2
    
    max_trial = len(one)*2 + 2
    count = 0
    
    # 반복문, 그리디?
    for _ in range(max_trial):
        if onesum > goal:
            temp = one.popleft()
            two.append(temp)
            onesum -= temp
            twosum += temp
            count += 1
            
        elif twosum > goal:
            temp2 = two.popleft()
            one.append(temp2)
            onesum += temp2
            twosum -= temp2
            count += 1
        
        if onesum == goal and twosum == goal:
            return count
        
    return -1
