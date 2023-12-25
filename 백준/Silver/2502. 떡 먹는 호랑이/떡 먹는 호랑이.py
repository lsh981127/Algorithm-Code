import sys

input = sys.stdin.readline
a, b = 1, 1

# a: 1일, b: 2일
d, num = map(int, input().split())

# 피노나치
first = list([0, 1])
second = list([1, 1])
for i in range(2, d-1):
	first.append(first[i-2] + first[i-1])
	second.append(second[i-2] + second[i-1])

while True:
	if a * first[-1] + b * second[-1] == num:
		break
	elif b * second[-1] < num:
		b += 1
	else:
		a += 1
		b = a

print(a)
print(b)