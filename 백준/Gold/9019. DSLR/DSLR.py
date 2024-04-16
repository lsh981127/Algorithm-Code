import sys
from collections import deque
input = sys.stdin.readline


def D(number):
    return (2*number) % 10000, 'D'

def S(number):
    if number == 0:
        return 9999, 'S'
    return number - 1, 'S'
    
def L(number):
    return number // 1000 + (number % 1000) * 10, 'L'
    
def R(number):
    return (number % 10) * 1000 + (number // 10), 'R'


test = int(input())
for _ in range(test):
    visited = [0] * 10001
    a, b = map(int, input().split())
    queue = deque()
    queue.append((a, ''))
    while queue:
        num, output = queue.popleft()
        if num == b:
            print(output)
            break
        
        for i, func in (D(num), S(num), L(num), R(num)):
            if not visited[i]:
                visited[i] = 1
                queue.append((i, ''.join([output, func])))
    