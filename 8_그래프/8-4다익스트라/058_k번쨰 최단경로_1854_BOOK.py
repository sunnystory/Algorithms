import sys
import heapq

input=sys.stdin.readline

N,M,K=map(int,input().split())

nodes=[[] for _ in range(N+1)]

distances=[[float('inf')]*K for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int, input().split())
    nodes[a].append((b,c))

q=[(0,1)]
distances[1][0]=0

while q:
    cost,node=heapq.heappop(q)
    for nNode, nCost in nodes[node]:
        distance= cost+nCost

        if distances[nNode][K-1]>distance:
            distances[nNode][K-1]=distance
            distances[nNode].sort()
            heapq.heappush(q,(distance,nNode))

for i in range(1,N+1):
    if distances[i][K-1]==float('inf'):
        print(-1)
    else:
        print(distances[i][K-1])