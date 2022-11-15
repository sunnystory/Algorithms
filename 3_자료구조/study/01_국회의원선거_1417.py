# import heapq
#
# N=int(input())
# li=[]
# ds=int(input())
# for i in range(N-1):
#     heapq.heappush(li,-int(input()))
# ans=0
# while True:
#     if len(li)==0:
#         break
#     k=-heapq.heappop(li)
#     print(k)
#     if k<ds:
#         break
#     else: #k>=ds:
#         dif=(k-ds)//2
#         ans+=dif
#         ds+=dif
#
# print(ans)
#


import heapq

N=int(input())
li=[]
ds=int(input())
for i in range(N-1):
    heapq.heappush(li,-int(input()))
ans=0
while True:
    if len(li)==0:
        break
    k=heapq.heappop(li)
    if -k>=ds:
        ans+=1
        k+=1
        ds+=1
        heapq.heappush(li,k)
    else:
        break
print(ans)

# 더 깔끔
import heapq

N = int(input())
D = int(input())
q = []
for _ in range(N-1):
    n = int(input())
    heapq.heappush(q, -n)
res = 0
while q:
    n = -heapq.heappop(q)
    if D > n:
        break
    D += 1
    res += 1
    heapq.heappush(q, -(n-1))
print(res)