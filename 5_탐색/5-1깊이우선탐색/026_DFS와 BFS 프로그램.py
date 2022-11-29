from collections import deque
N,M,V=map(int,input().split())
# V=int(input())

arr=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)

visited=[]
needvisit=deque([])

# 자꾸하는 실수**********
# def bfs(v):
#     needvisit.append(v)
#     while needvisit:
#         x=needvisit.popleft()
#         visited.append(x)
#         for _ in arr[x]:
#             if _ not in visited:
#                 needvisit.append(_)
#     return visited

def bfs(v):
    needvisit.append(v)
    visited.append(v)
    while needvisit:
        x=needvisit.popleft()
        # visited.append(x)
        for _ in arr[x]:
            if _ not in visited:
                visited.append(_)
                needvisit.append(_)

    return visited



def dfs(v):
    visited.append(v)
    arr[v]=sorted(arr[v]) #.sort()
    for i in arr[v]:
        if i not in visited:
            dfs(i)



dfs(V)
for i in visited:
    print(i,end=' ')
print()
visited=[]
bfs(V)
for i in visited:
    print(i,end=' ')



