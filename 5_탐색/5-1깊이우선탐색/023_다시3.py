import sys

input=sys.stdin.readline
sys.setrecursionlimit(10000)

n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited=[False]*(n+1)
#재귀 dfs는 visited 리스트만 있으면 됨- needvisit 구현 필요 없음
def dfs(x):
    #방문 하고
    visited[x]=True
    ##방문한것과 연결된 노드들 탐색
    ###(chain 식으로 깊게 탐색하기 위해 재귀함수 사용-dfs)
    #연결된 노드들 중에서
    for i in nodes[x]:
        #방문 안한게 있으면
        if not visited[i]:
            # 방문 처리하고
            # 관련 된 노드들 더 깊게 들어가서 방문 처리하고...
            # 재귀로 구현 - dfs
            dfs(i)

#needvisit 이 아니라 visited여부로 다음 노드 탐색 할건지 풀어야함
#needvisit은 노드 간에 공통으로 연결된 노드들이 많아서
#needvisit 내에 노드들은 계속 중복으로 저장 될 수 있음
#그런 needvisit중에 visited 안됐는지를 확실히 체크한 후에 방문해야함!

count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)