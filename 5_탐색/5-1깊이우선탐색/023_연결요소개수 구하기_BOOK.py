n,m=map(int,input().split())

A=[[] for _ in range(n+1)]
visited=[False] * (n+1)

def DFS(v):
    visited[v]=True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s,e =map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count=0

#노드 돌아가면서 확인
for i in range(1,n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)