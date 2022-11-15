# n=int(input())
#
# import heapq
# score=[]
# for i in range(n):
#     t,s=map(int, input().split())
#     heapq.heappush(score,(-t,-s))
#
# mt,ms=heapq.heappop(score)
#
# num=-mt
# total=-ms
#
# print(num,total)
# while score:
#     t,s=heapq.heappop(score)
#     t,s=-t,-s
#     print(t,s)
#     if t<num:
#        print(t,s)
#        total+=s
#        num-=1
#     else:
#         pass
#
# print(total)
#
# g

n=int(input())

import heapq
score=[]
for i in range(n):
    t,s=map(int, input().split())
    heapq.heappush(score,(-t,-s))

mt,ms=heapq.heappop(score)

num=-mt
total=-ms

pre=[]
for i in range(num-1,0,-1): #5,4,3,2,1
    if len(score)!=0:
        t,s=heapq.heappop(score)
        while -t>=i and len(score)!=0:
            heapq.heappush(pre,(s,t))
            t, s = heapq.heappop(score)

        ''' DIBUGGING!!!!
        heapq 저장 배열에는 시간이 아니고 과제 점수가 우선순위가 되도록 구현!!!
        '''
        if -t>=i :
            heapq.heappush(pre, (s,t))
        else:
            heapq.heappush(score,(t,s))

    if len(pre)!=0:
        ss,st=heapq.heappop(pre)
        total+=-ss

print(total)
