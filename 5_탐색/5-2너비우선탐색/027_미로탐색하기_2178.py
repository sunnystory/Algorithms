# # 시도 1
# import sys
# input=sys.stdin.readline
# n,m=map(int,input().split())
#
# arrs=[list(map(int,list(input().strip()))) for _ in range(n)]
#
# a=[0,1,0,-1]
# b=[1,0,-1,0]
#
# need_visit=[(0,0)]
# visited=[[0]*m for _ in range(n)]
#
# num=0
# def dfs():
#     global num
#     while need_visit:
#         x,y=need_visit.pop()
#         if x==n-1 and y==n-1:
#             num+=1
#             return
#         if visited[x][y]==0:
#             visited[x][y]=1
#             num+=1
#
#             for i in range(4):
#                 x_n,y_n=x+a[i],y+b[i]
#                 if x_n>0 and y_n>0 and arrs[x_n][y_n]==1:
#                     need_visit.append((x_n,y_n))
#                     dfs()
#
# dfs()
# print(num)
#
#


# print(arrs)
#
# # 시도 2
# from collections import deque
#
# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
#
# N,M=map(int,input().split())
# A=[[0]*M for _ in range(N)]
# visited=[[False]*M for _ in range(N)]
#
# for i in range(N):
#     numbers=list(input())
#     for j in range(M):
#         A[i][j]=int(numbers[j])
#
# def BFS(i,j):
#     queue=deque()
#     queue.append((i,j))
#     visited[i][j]=True
#     while queue:
#         node=queue.popleft()
#         x,y=node
#         for l in range(4):
#             xn,yn=x+dx[l],y+dy[l]
#             if xn>=0 and yn>=0 and x<N and y<M:
#                 if A[xn][yn]!=0 and not visited[xn][yn]:
#                     visited[xn][yn]=True
#                     A[xn][yn]=A[x][y]+1
#                     queue.append((xn,yn))
#
# BFS(0,0)
# print(A[N-1][M-1])



# 시도 3
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
        for l in range(4):
            xn,yn=x+dx[l],y+dy[l]
            if xn>=0 and yn>=0 and xn<N and yn<M:
                if A[xn][yn]!=0 and not visited[xn][yn]:
                    visited[xn][yn]=True
                    A[xn][yn]=A[x][y]+1
                    queue.append((xn,yn))

BFS(0,0)
print(A[N-1][M-1])
