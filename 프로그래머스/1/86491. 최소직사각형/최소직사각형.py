def solution(sizes):
# 그냥 1개 큰 값들로 정렬(회전시켜서)
# 그 다음 그 중 최댓값 X 반대값 중 최댓값 
    big = set()
    small = set()
    for length in sizes:
        big.add(max(length[0], length[1]))
        small.add(min(length[0], length[1]))
    return int(max(big)) * int(max(small))
        