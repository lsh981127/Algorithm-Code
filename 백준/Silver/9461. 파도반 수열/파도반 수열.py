import sys
input = sys.stdin.readline

def func(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    
    if n == 4 or n == 5:
        return 2
    
    
    
    return func(n-1) + func(n-5)

t = int(input())
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]
    
for _ in range(t):
    n = int(input())
    print(dp[n])