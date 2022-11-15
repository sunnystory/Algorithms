# # BFS
# from collections import deque
# N,M,V=map(int,input().split())
#
# nodes=[[]for _ in range(N+1)]
# for _ in range(M):
#     n,m=map(int,input().split())
#     nodes[n].append(m)
#     nodes[m].append(n)
#
# visited=[False]*(N+1)
# needvisit=deque()
# needvisit.append(V)
# visited[V]=True
#
#
# def bfs():
#     while needvisit:
#         x=needvisit.popleft()
#         print(x,end=' ')
#
#         #sort 위치!!
#         nodes[x].sort()
#         for _ in nodes[x]:
#
#             # 순서 **
#             # 1. visited 안됐는지 확인하고
#             if not visited[_]:
#                 # 2. needvist 에 넣고
#                 needvisit.append(_)
#                 # 3. visit=True 해야함!! (***)
#                 visited[_]=True
#
#
#
# def dfs():
#     while needvisit:
#         x=needvisit.pop()
#         print(x,end=' ')
#         nodes[x].sort()
#         for _ in nodes[x]:
#             if not visited[_]:
#                 visited[_]=True
#                 needvisit.append(_)
#                 dfs()
# dfs()
# visited=[False]*(N+1)
# needvisit=deque()
# needvisit.append(V)
# visited[V]=True
# print()
# bfs()





########################
# dfs 는 visited
# BFS
from collections import deque
N,M,V=map(int,input().split())

nodes=[[]for _ in range(N+1)]
for _ in range(M):
    n,m=map(int,input().split())
    nodes[n].append(m)
    nodes[m].append(n)

visited=[False]*(N+1)
needvisit=deque()
# needvisit.append(V)
# visited[V]=True

def dfs(x):
    print(x, end=' ')
    nodes[x].sort()
    visited[x] = True
    for _ in nodes[x]:
        if not visited[_]:
            dfs(_)
dfs(V)
visited=[False]*(N+1)
print()

def bfs(x):
    needvisit.append(x)
    visited[x]=True
    while needvisit:
        node=needvisit.popleft()
        print(node, end=' ')
        nodes[node].sort()
        for i in nodes[node]:
            if not visited[i]:
                visited[i]=True
                needvisit.append(i)

bfs(V)

