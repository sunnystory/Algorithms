N,M=map(int,input().split())

# nodes=[[0]]*N
nodes=[[] for _ in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)

node_check=[x for x in range(1,N+1)]
# print(node_check)

def dfs(x):
    needvisit=[x]
    visited=[]
    while needvisit:
        new=needvisit.pop()

        #needvisit이 아니라 needvisit에 있는 걸 visited에 넣을때 visited했는지 검사를 해야되는 것******
        #여기서 DIBUGGING!!!!!!!!!
        visited.append(new) #VISITED 넣기 전에!!!! needvisit에서 꺼낸 원소가 방문 된건지 검사!!!!!!!
        # print(new)
        # node_check.remove(new)
        new_nodes=nodes[new]
        for i in new_nodes:
            if i not in visited:
                needvisit.append(i)

def dfs(x):
    needvisit=[x]
    visited=[]
    while needvisit:
        new=needvisit.pop()
        # visited.append(new)
        # print(new)
        if new not in visited:
            visited.append(new)
            # node_check.remove(new)
            needvisit.extend(nodes[new])

        # node_check.remove(new)
        # new_nodes=nodes[new]
        # for i in new_nodes:
        #     if i not in visited:
        #         needvisit.append(i)


#FALSE
# 이런 방식은 시간초과
dfs(1)
count=1
while node_check:
    count+=1
    for i in node_check:
        dfs(i)

print(count)

#모든 노드를 탐색하는 데 실행한 DFS의 실행 횟수가 곧 연결 요소 개수와 같다.
## dfs가 한번 실행될때마다 count+=1

for i in range(N):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)