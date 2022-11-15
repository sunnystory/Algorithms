#처음 시도

V,E=map(int,input().split()) #노드개수, 에지개수
K=int(input()) #시작 노드

nodes=[[] for _ in range(V+1)]
# 시작점->다른 모든 노드로의 최단경로
for _ in range(E):
    u,v,w=map(int,input().split())
    nodes[u].append((v,w))

# print(nodes)
distances=[float('inf') for _ in range(V+1)]
distances[K]=0
needvisit=[]
needvisit.extend(nodes[K])
print(needvisit,'1')
# print(needvisit)
visited=[False]*(V+1)
visited[K]=True
#visited는 왜 필요한가??

while needvisit:
    node, weight=needvisit.pop() #3,3  #2,2
    # print(needvisit,node,weight,'pop') #[],2,2
    # visited[node]=True

    if distances[node] < weight + distances[node]:  #????
        continue
    if not visited[node]:
        distances[node]=weight #distances[3]=3 ...
    # distances[node]=weight + distances[node] #3+inf

    for order in range(len(nodes[node])): #1
        v,w=nodes[node][order] #4,6
        new_route=weight+w #new=weight+4=7

        if distances[v] > new_route:
            print(new_route)
            distances[v]=new_route #distances[4]=7

            #새롭게 노드 추가
            if not visited[v]:
                # print(nodes[v])
                # print(needvisit,'ndv')
                for i in range(len(nodes[v])):
                    #i
                    needvisit.append((nodes[v][i][0],nodes[v][i][1]+w))
                # needvisit.extend(nodes[v])
                # print(needvisit)
                visited[v]=True

print(distances[1:])

    # 현재 값이 가장 작은 노드


