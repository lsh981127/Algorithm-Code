import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = {}
for _ in range(N):
    add, password = input().strip().split()
    memory[add] = password

for _ in range(M):
    add = input().strip()
    print(memory[add])