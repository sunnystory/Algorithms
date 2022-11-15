

from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

N,M=map(int,input().split())
A=[[0]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]

for i in range(N):
    numbers=list(input())
    for j in range(M):
        A[i][j]=int(numbers[j])

def BFS(i,j):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True

    while queue:
        node=queue.popleft()
        x,y=node


        for i in range(4):
            xn,yn=x+dx[i],y+dy[i]
            if 0<=xn<N-1 and 0<=yn<M-1:
                if numbers[xn][yn]==1 and not visited[xn][yn]:
                    visited[xn][yn]=True
                    numbers[xn][yn]=A[x][y]+1
                    queue.append((xn,yn))

BFS(0,0)
print(A[N-1][M-1])