from itertools import combinations
def solution(orders, course):
    people = []
    answer = []
    for i in orders:
        tmp = list(str(i))
        tmp.sort()
        # 마지막 예제 XWY, WXA에서 XW, WX 가 다르게 되서
        # 처음 list화 할때부터 sort 시키기
        people.append(tmp)
    
    
    for i in course:
        result = {}
        for j in people:
            if len(j) < i: # course 길이보다 작으면 제거
                continue
            comb = list(map(''.join, combinations(j, i)))
            # combination 출력시 ('a', 'b','c') 
            # 이렇게 튜플 형식으로 출력
            # 이걸 1개 문자열로 합치기
            for k in comb:
                temp = str(k)
                if k not in result:
                    result[temp] = 1
                else:
                    result[temp] += 1
                    
        # max_course = max(result, key=result.get) 
        # 최대 value를 가지는 keys
        # max 써서 할때는 최댓값이 여러개인 경우 못 가져온다
        # 리스트 컴프리헨션을 사용해야함
        
        max_list = [a for a,v in result.items() if max(result.values()) == v and v > 1]
        # v > 1 없이 했는데 지문에서 2명 이상이 주문해야 포함해야함
        
        
        answer.extend(max_list)
    answer.sort()
    
    return answer