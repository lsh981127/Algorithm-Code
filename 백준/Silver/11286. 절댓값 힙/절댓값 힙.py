import heapq, sys
input = sys.stdin.readline


N = int(input())
plus_arr = []
minus_arr = []

for _ in range(N):
    temp = int(input())
    if temp != 0:
        if temp > 0:
            heapq.heappush(plus_arr, temp)
        else:
            heapq.heappush(minus_arr, -1 * temp)
    else:
        if not plus_arr and not minus_arr:
            print(0)
        elif not plus_arr:
            print((-1)*(heapq.heappop(minus_arr)))
        elif not minus_arr:
            print(heapq.heappop(plus_arr))
        else:
            x = plus_arr[0]
            y = minus_arr[0]

            if x >= y:
                if minus_arr:
                    print((-1)*(heapq.heappop(minus_arr)))
            elif x < y:
                print(heapq.heappop(plus_arr))