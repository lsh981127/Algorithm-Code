def solution(numbers):
    order = sorted(numbers, key=lambda x: str(x)*3, reverse=True) # 제일 앞자리 기준으로 정렬
    order = list(map(str, order))
    return str(int(''.join(order)))
    
    
    
        