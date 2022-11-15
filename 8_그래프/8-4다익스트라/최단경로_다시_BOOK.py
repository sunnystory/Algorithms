import sys
input=sys.stdin.readline
import heapq

V,E= map(int,input().split())
K=int(input())

distance=[float('inf')]*(V+1)
visited=[False] * (V+1)


myList=[[] for _ in range(V+1)]
q=[]

for _ in range(E):
    u,v,w=map(int,input().split())
    myList[u].append((v,w))

# 첫 노드 설정
heapq.heappush(q,(0,K)) #거리 0, 시작점 K
distance[K]=0

while q: ###
    current=heapq.heappop(q)
    c_v=current[1]

    # if visited[c_v]:
    #     continue
    if distance[c_v] < current[0]:  # <=
        continue

    # #방문되지 않은 정점의 경우
    # visited[c_v]=True
    #인접 정점까지 거리 구하기, 인접 정점까지 최단 거리 업데이트,방문할 q 업데이트
    for tmp in myList[c_v]:
        next,value=tmp[0],tmp[1]
        if distance[next]>distance[c_v]+value:
            # 인접 정점 최단거리 업데이트
            distance[next]=distance[c_v]+value
            # 우선순위큐에 저장, (가중치, 노드) 순으로
            heapq.heappush(q,(distance[next],next))

for i in range(1,V+1):
    if distance[i] != float('inf'):
        print(distance[i])
    else:
        print('INF')

