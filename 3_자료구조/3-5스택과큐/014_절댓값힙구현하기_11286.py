from collections import deque

N=int(input())
arr=deque()

for i in range(N):
    k=int(input())
    # print(k,'k')
    if k==0:
        if len(arr)==0:
            print(0)
        else:
            # print(arr.popleft())
            print(arr.pop(0))
    else:
        arr.append(k)
        arr=sorted(arr, key=lambda x:(abs(x),x))
        # arr=sorted(arr, key=lambda x:abs(x))
        # print(arr)