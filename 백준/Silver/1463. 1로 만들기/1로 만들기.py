import sys
input = sys.stdin.readline

val = int(input())

# 바텀업
dp = [0] * (val+1)

for i in range(2, val+1):
    dp[i] = dp[i-1] + 1 # 우선 -1을 한 걸로 초기화
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        # 그냥 / 를 쓰면 float 자료형으로 인식해서 // 로 확실하게 int로 만들어주기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[val])