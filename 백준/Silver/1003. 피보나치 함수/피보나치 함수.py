import sys
input = sys.stdin.readline

# f(0), f(1), f(2) 일때 각 갯수
list_0 = [1,0,1]
list_1 = [0,1,1]

def fibo(num):
    list_0 = [1,0,1]
    list_1 = [0,1,1]
    if num >= 3:
        for i in range(2, num): # 2부터 num-1까지 돌려야 f(num) = f(num-2) + f(num-1)로 최종 num까지 갯수 고려한 게 됨
            list_0.append(list_0[i-1] + list_0[i])
            list_1.append(list_1[i-1] + list_1[i])
    print(f"{list_0[num]} {list_1[num]}")

# 0과 1 값들도 피보나치 연산처럼 갯수 합산

t = int(input())
for _ in range(t):
	val = int(input())
	fibo(val)
