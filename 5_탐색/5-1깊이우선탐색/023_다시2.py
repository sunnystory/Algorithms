import sys
input=sys.stdin.readline
# sys.setrecursionlimit(10000)

n,m=map(int,input().split())
#초기화 그래프 만들기
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

needvisit=[]
visited=[False]*(n+1)
needvisit=[]
#stack으로 구현하기
def dfs(x):
    # visited[i]=True
    needvisit.append(x)
    while needvisit:
        # dfs는 스택 기법으로 나중에 들어온거 먼저 뽑기로 체인식 dfs 구현
        # needvisit에서 뒤에서부터 뺴야함
        i=needvisit.pop()
        if not visited[i]:
            visited[i]=True
            needvisit.extend(nodes[i])

count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)


