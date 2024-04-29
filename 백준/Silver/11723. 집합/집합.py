import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    temp = input().split()
    
    if len(temp) != 1:
        func, num = temp[0], temp[1]
        num = int(num)
        if func == 'add':
            if num not in arr:
                arr.add(num)
        elif func == 'remove':
            if num in arr:
                arr.remove(num)
        elif func == 'check':
            if num in arr:
                print(1)
            else:
                print(0)
        elif func == 'toggle':
            if num in arr:
                arr.remove(num)
            else:
                arr.add(num)
    else:
        func = temp[0]
        if func == 'all':
            arr = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
        else:
            arr = set()