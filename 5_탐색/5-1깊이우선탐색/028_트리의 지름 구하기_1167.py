# from collections import deque
#
# v=int(input())
#
# arr=[[] for _ in range(v)]
#
# for _ in range(v):
#     new=list(map(int,input().split()))[:-1]
#     a=new[0]
#     tree=new[1:]
#     len=tree//2
#     for i in range(len):
#         k=i*2
#         b,c=tree[k:k+2]
#         arr[a].append((b,c)) # 노드, 가중치
#
#         arr[b].append(a,c)
#
#
# def bfs(x):
#     visited=[x]
#     needtovisit=deque([(x,0)])
#     distances=[[0]*(v+1) for _ in range(v+1)]
#
#     while needtovisit:
#         a,w=needtovisit.popleft()
#
#         for i in arr[a]:
#             b,w2=i
#             if b not in visited:
#                 needtovisit.append(i)
#                 visited.append(i)
#                 if w2+w > distances[b]:
#                     distances[i]=w2+w
#
#
#
# for _ in range(v):
#     bfs()



from collections import deque

N=int(input())
A=[[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int,input().split()))
    index=0
    S=Data[index]
    index+=1
    while True:
        E=Data[index+1]
        if E==-1:
            break
        V=Data[index+1]
        A[S].append((E,V))
        index+=2

distance=[0]*(N+1)
visited=[False]*(N+1)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now_Node=queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]]=True
                queue.append(i[0])
                distance[i[0]]=distance[now_Node]+i[1]

BFS(1)
Max=1

for i in range(2,N+1):
    if distance[Max] <distance[i]:
        Max=i

distance=[0]*(N+1)
visited=[False]*(N+1)
BFS(Max)
distance.sort()
print(distance[N])









