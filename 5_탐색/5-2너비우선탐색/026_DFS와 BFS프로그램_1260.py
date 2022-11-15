#노드 번호가 작은 것 먼저 방문
import sys
input=sys.stdin.readline

# import sys.setrecursionlimit(10000)
sys.setrecursionlimit(10000)

#***#
from collections import deque

n,e,s=map(int,input().split())
nodes=[[] for _ in range(n+1)]

for _ in range(e):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)


def bfs(x):
    needvist.append(x)
    while needvist:
        i=needvist.popleft()
        if i not in visited:
            visited.append(i)
            print(i,end=' ')
            nodes[i].sort()
            needvist.extend(nodes[i])
    return visited

def dfs(x):
    visited.append(x)
    print(x,end=' ')
    nodes[x].sort()
    for i in nodes[x]: #nodes(x) 아님 주의!!!!!!! 디버깅 요소!! nodes[x]임!!!
        if i not in visited:
            dfs(i)
    return visited

visited=deque()
needvist=deque()
dfs(s)
print()#'\n',end=''
visited=deque()
needvist=deque()
bfs(s)



# # print(dfs(1))
# print(i for i in visited)
# visited=deque()
# needvist=deque()
# # print(bfs(1))
# print(i for i in visited)
