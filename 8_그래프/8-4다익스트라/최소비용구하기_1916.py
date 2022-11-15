import heapq
n=int(input())
m=int(input())
nodes=[[] for _ in range(n+1)]
distances=[float('inf') for _ in range(n+1)]
for _ in range(1,m+1):
    a,b,w= map(int,input().split())
    nodes[a].append((b,w))

A,B=map(int,input().split())

distances[A]=0
q=[]

heapq.heappush(q,(0,A))
# for _ in nodes[A]:
#     i,j=_
#     heapq.heappush(q,(j,i))

while q:
    weight,node=heapq.heappop(q)
    if distances[node]<weight:
        continue
    # distances[node]=weight
    for _ in nodes[node]:
        new_nd,new_wg=_
        distance=new_wg+weight
        if distance < distances[new_nd]:
            distances[new_nd]=distance
            heapq.heappush(q,(distance,new_nd))


print(distances[B])
