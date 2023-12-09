import sys
from collections import deque
input = sys.stdin.readline

# intValue = map(int, input())
intValue = int(input())
arr = list(map(int, str(intValue)))
# intValue의 길이는 항상 짝수

front = 0
back = 0
half = len(arr) // 2
front += sum(arr[:half])
back += sum(arr[half:])
if front == back:
    print("LUCKY")
else:
    print("READY")