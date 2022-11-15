import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
#초기화 그래프 만들기
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

needvisit=[]
visited=[False]*(n+1)

# def dfs(x):
#     needvisit.append(x)
#     while needvisit:
#         i=needvisit.pop()
#         if not visited[i]:
#             visited[i]=True
#             for i in nodes[i]:
#                 dfs(i)
#             # needvisit.extend(nodes[i])


def dfs(x):
    visited[x]=True

    #needvisit 역할
    for i in nodes[x]:
        if not visited[i]:
            dfs(i)

# dfs(1)
# count=1
count=0
for i in range(1,n+1):
    if visited[i]== False:
        dfs(i)
        count+=1

print(count)





