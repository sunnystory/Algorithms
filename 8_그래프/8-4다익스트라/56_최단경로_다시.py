import heapq
#heapq 우선순위큐 사용 예시
import heapq
#hq=[]
#push : heapq.heappush(hq,item)
#pop : heapq.heappop(hq)
#heapify(hq)


V,E=map(int,input().split())
K=int(input())
nodes=[[] for _ in range(V+1)]
# 시작점->다른 모든 노드로의 최단경로
for _ in range(E):
    u,v,w=map(int,input().split())
    nodes[u].append((w,v)) #순서 주의

# print(nodes)
distances=[float('INF') for _ in range(V+1)]
distances[K]=0

hq=[]
heapq.heappush(hq,(0,K))
# hq.extend(nodes[K]) #수정
# print(hq)

#visited 왜 필요한지???

while hq:
    w,v=heapq.heappop(hq)
    # print(w,v,'1번힙팝')

    if distances[v]<w:  #<=
        continue

    # DIBUGGIND : 이거 여기 넣으면 안돼!!!!!!!!!
    # 거리 업데이트는 이미 인접노드에서 큐로 넣을때 이뤄져야한다고
    # 큐에서 뺄때는 거리 업데이트 안해!!!!
    # distances[v]=w

    for tmp in nodes[v]:
        new_w,new_v=tmp
        # print(new_w,new_v,'2')
        # distance = w + new_w
        distance= w + new_w
        # print(distance,'3')
        if distance<distances[new_v]:
            ####여기 틀림 - 업데이트 뺴먹음@@@!!
            distances[new_v] = distance
            #################################
            heapq.heappush(hq,(distance,new_v))

# print(distances[1:])

for i in distances[1:]:
    if i==float('inf'):
        print('INF')
    else:
        print(i)
