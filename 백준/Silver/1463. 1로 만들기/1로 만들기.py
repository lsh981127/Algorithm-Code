import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
val = int(input())

# 바텀업


# for i in range(2, val+1):
#     dp[i] = dp[i-1] + 1 # 우선 -1을 한 걸로 초기화
    
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3] + 1)
#         # 그냥 / 를 쓰면 float 자료형으로 인식해서 // 로 확실하게 int로 만들어주기
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2] + 1)

# print(dp[val])


# 탑다운
# 재귀 + 매모리제이션

# def top(dp, value):
#     if dp[value] != -1:
#         return dp[value]
    
#     if value % 3 == 0 and value % 2 == 0:
#         dp[value] = 1 + min(top(dp, value // 3), top(dp, value // 2))
#     elif value % 3 == 0:
#         dp[value] = 1 + min(top(dp, value - 1), top(dp, value//3))
#     elif value % 2 == 0:
#         dp[value] = 1 + min(top(dp, value - 1), top(dp, value // 2))
#     else:
#         dp[value] = 1 + top(dp, value-1)
    
#     return dp[value]

def top(value):
    if dp[value] != -1:
        return dp[value]
    
    if value % 3 == 0 and value % 2 == 0:
        dp[value] = 1 + min(top(value // 3), top(value // 2))
    elif value % 3 == 0:
        dp[value] = 1 + min(top(value - 1), top(value//3))
    elif value % 2 == 0:
        dp[value] = 1 + min(top(value - 1), top(value // 2))
    else:
        dp[value] = 1 + top(value-1)
    
    return dp[value]

dp = [-1] * (val+1)
dp[1] = 0
print(top(val))