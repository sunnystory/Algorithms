import sys
input=sys.stdin.readline
import heapq

n,m,k=map(int,input().split())
nodes=[[] for _ in range(n+1)]

distances=[[float('inf')]*k for _ in range(n+1)]


for _ in range(m):
    a,b,c=map(int,input().split())
    nodes[a].append((b,c)) #node, weight


distances[1][0]=0
q=[(0,1)]

while q:
    w,n=heapq.heappop(q)

    # # 이거 빠져야함- 같은 노드 다른 거리 중복 돼서 넣어져야 하므로
    # if distances[n]<w:
    #     continue

    for node, weight in nodes[n]:
        distance=weight + w

        if distances[node][k-1]> distance:

            distances[node][k-1]=distance
            distances[node].sort()
            heapq.heappush(q,(distance, node))
# print(distances)

for i in range(1,n+1):
    if distances[i][k-1] == float('inf'):
        print(-1)
    else:
        print(distances[i][k-1])






