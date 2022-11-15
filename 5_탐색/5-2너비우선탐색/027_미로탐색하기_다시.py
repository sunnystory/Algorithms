# import sys
# sys.setrecursionlimit(10**6)
# N,M=map(int,input().split())
# arr=[]
# for i in range(N):
#     arr.append(list(map(int, list(input()))))
#
# A=[[0]*M for _ in range(N)]
#
# visited=[[0]*M for _ in range(N)]
#
#
# dx=[1,0,0,-1]
# dy=[0,1,-1,0]
#
#
# # needvisit=[]
#
#
# def dfs(x,y,num):
#     visited[x][y]=1
#     num+=1
#
#     if arr[x][y]==1:
#         for _ in range(4):
#             n_x=dx[_]+x
#             n_y=dx[_]+y
#
#             if n_x==N-1 and n_y==N-1:
#                 print(num)
#                 return
#
#             if n_x>=0 and n_x<N and n_y>=0 and n_y<N:
#                 dfs(n_x,n_y,num)
#
# dfs(0,0,0)


# dfs 구현도 틀리고 , dfs로 하면 최단거리가 안될 수 있음 주의
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int, list(input()))))

visited=[[0]*M for _ in range(N)]


dx=[1,0,0,-1]
dy=[0,1,-1,0]


# needvisit=[]


def dfs(x,y):
    visited[x][y]=1
    #
    # if arr[x][y]==1:
    for _ in range(4):
        n_x=dx[_]+x
        n_y=dy[_]+y

        # if n_x==N-1 and n_y==N-1:
        #     print(num)
        #     return

        if n_x>=0 and n_x<N and n_y>=0 and n_y<M :
            if arr[n_x][n_y]==1 and visited[n_x][n_y]==0 :
                visited[n_x][n_y]=1
                arr[n_x][n_y]=arr[x][y]+1
                dfs(n_x,n_y)

dfs(0,0)
print(arr[-1][-1])
print(arr)

# => dfs는 최선의 경로가 아닐 수 있음... 하나 꽃혀서 가지는 걸로 최단경로로 간주해서 구하게 됨 => visited 다 되버리면 종료됨.



#bfs 로 다시
# from collections import deque
# N,M = map(int,input().split())
# arr=[]
# for i in range(N):
#     arr.append(list(map(int, list(input()))))
# # A=[[0]*M for _ in range(N)]
# visited=[[0]*M for _ in range(N)]
#
# dx=[1,0,0,-1]
# dy=[0,1,-1,0]
#
# def bfs(x,y):
#     needvisit = deque()
#     needvisit.append((0,0))
#     visited[0][0]=1
#     while needvisit:
#         x,y=needvisit.popleft()
#
#         for i in range(4):
#             nx,ny=x+dx[i],y+dy[i]
#
#             if nx>=0 and nx<N and ny>=0 and ny<M:
#                 if visited[nx][ny]==0 and arr[nx][ny]>0: #==1:
#                     needvisit.append((nx,ny))
#                     visited[nx][ny]=1
#                     arr[nx][ny]=arr[x][y]+1
#
# bfs(0,0)
# print(arr[-1][-1])




