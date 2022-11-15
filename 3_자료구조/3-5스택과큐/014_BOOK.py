import heapq
import sys
input=sys.stdin.readline
# from collections import deque

N=int(input())
arr=[]

for i in range(N):
    k=int(input())
    # print(k,'k')
    if k==0:
        if len(arr)==0:
            print(0)
        else:
            # print(arr.popleft())

            print(heapq.heappop(arr)[1])
            # print(heapq.heappop(arr))

            # print(arr.pop(0))
    else:
        # arr.append(k)

        heapq.heappush(arr,(abs(k),k))
        # heapq.heappush(arr, ((abs(k), k),k))


        # arr=sorted(arr, key=lambda x:(abs(x),x))
        # arr=sorted(arr, key=lambda x:abs(x))
        # print(arr)

