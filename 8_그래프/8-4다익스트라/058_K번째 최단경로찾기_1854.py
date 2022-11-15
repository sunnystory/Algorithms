# 최단경로 일반
# #n,m,k 도시개수, 도로수, (a,b,w),
# import sys
# input=sys.stdin.readline
# import heapq
#
# n,m,k=map(int,input().split())
#
# #노드 만들기
# node=[[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,w=map(int,input().split())
#     node[a].append((b,w))
# #우선순위 큐
# q=[]
# heapq.heappush(q,(0,1)) #weight, node
# #거리
# distances=[float('inf') for _ in range(n+1)]
#
# while q:
#     w,n=heapq.heappop(q)
#
#     #=은 포함해도 되는지(?)
#     if w>distances[n]:
#         continue
#
#     for _ in node[n]:
#         #디버깅! => node 부분은 node, weight순으로 저장했음....ㅠ
#         new_n,new_w=_
#         distance=new_w+w
#         if distance<distances[new_n]:
#             distances[new_n]=distance
#             heapq.heappush(q,(distance,new_n))
#
# print(distances[1:])
#


# k번째 최단경로
#n,m,k 도시개수, 도로수, (a,b,w),
import sys
input=sys.stdin.readline
import heapq

n,m,k=map(int,input().split())

#노드 만들기
node=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,w=map(int,input().split())
    node[a].append((b,w))
#우선순위 큐
q=[]
heapq.heappush(q,(0,1)) #weight, node
#거리
distances=[[float('inf') for _ in range(n+1)] for _ in range(k)]
distances[0][1]=0

while q:
    w,n=heapq.heappop(q)

    #=은 포함해도 되는지(?)
    num=0
    # if w>distances[0][n]:
    #     num += 1
    #     while num >= k and w>distances[num][n]:
    #         continue

    while num < k and w>distances[num][n]:
        num += 1

    if w>distances[num][n]:
        continue

    for _ in node[n]:
        num = 0
        #디버깅! => node 부분은 node, weight순으로 저장했음....ㅠ
        new_n,new_w=_
        distance=new_w+w
        if distance>=distances[num][new_n]:
            while distance<distances[num][new_n] and num<k:
                num+=1

        elif distance<distances[num][new_n]:
            distances[num][new_n]=distance
            heapq.heappush(q,(distance,new_n))

print(distances[k-1][1:])

