import sys

input = sys.stdin.readline

name_dict = {}
index_dict = {}

N, M = map(int, input().split())

# for i in range(N):
#     temp = str(input())
#     hashVal = hash(temp)
#     if hashVal not in hash_dict:
#         hash_dict[hashVal] = (i, temp)  # index, hash 값 형태의 튜플을 dict에 저장
    
# for _ in range(M):
#     # str인지 int인지 구분해야하는 것 같은데..
#     check = str(input()) # 일단 문자열로 검사
#     if not int(check):
#         print(hash_dict[hash(check)])
#     else:
#         print(hash_dict.items())



# 직접 hash 써서 만들어보려 했는데 실패....
# 그냥 맘 편하게 dict 2개 써서 하면 

for i in range(1,N+1):
    temp = input().split()[0]
    name_dict[temp] = i
    index_dict[i] = temp

for _ in range(M):
    tr = input().split()[0]
    if tr.isalpha(): # 문자열이 문자열이면, 문자열이 숫자이면은 .isdigit
        print(name_dict[tr])
    else: # 숫자야
        print(index_dict[int(tr)])