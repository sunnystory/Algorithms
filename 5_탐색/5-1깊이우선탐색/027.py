# from collections import deque
# import copy
#
# N,M=map(int, input().split())
#
# arr=[]
#
# for i in range(N):
#     for j in range(M):
#         arr.append(list(map(int,list(str(input())))))
#
# #그리드 최단거리는 bfs로
# #dfs로 하면 최단거리가 아니게 도달 할 수 있음
#
# visited=copy.deepcopy(arr)
#
# def bfs():
#     # visited=[]
#     needvisit=deque([])
#     needvisit.append([0,0])
#     arr[0][0]=0
#     cnt=1
#     x=[1,-1,0,0]
#     y=[0,0,1,-1]
#     while needvisit:
#         a,b=needvisit.popleft()
#         for i in range(4):
#             na=a+x[i]
#             nb=b+y[i]
#
#             if na==N-1 and nb==M-1:
#                 return cnt+1
#
#             if arr[na][nb] == 1:
#                 needvisit.append([na,nb])
#                 arr[na][nb]=0
#                 cnt+=1
#
#
#
#
# print(bfs())

from collections import deque
# import copy

N,M=map(int, input().split())

arr=[[0]*M for _ in range(N)]

# for i in range(N):
#     for j in range(M):
#         arr.append(list(map(int,list(str(input())))))

for i in range(N):
    numbers=list(input())
    for j in range(M):
        arr[i][j]=int(numbers[j])
# print(arr)
#그리드 최단거리는 bfs로
#dfs로 하면 최단거리가 아니게 도달 할 수 있음

# visited=copy.deepcopy(arr)
visited=[[False]*M for _ in range(N)]
def bfs():
    # visited=[]
    needvisit=deque([])
    needvisit.append([0,0])
    visited[0][0]=True
    cnt=1
    x=[1,-1,0,0]
    y=[0,0,1,-1]
    while needvisit:
        a,b=needvisit.popleft()
        for i in range(4):
            na=a+x[i]
            nb=b+y[i]

            # if na==N-1 and nb==M-1:
            #     return cnt+1

            #DIBUGGINGGGGGGGG
            if na>=0 and nb>=0 and na<N and nb<M:
                if arr[na][nb] == 1 and not visited[na][nb]:
                    needvisit.append([na,nb])
                    visited[na][nb]=True
                    # arr[na][nb]+=1
                    arr[na][nb]=arr[a][b]+1
bfs()

print(arr[N-1][M-1])