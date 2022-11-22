# # 0~N-1
#
# import sys
# sys.setrecursionlimit(1000000)
# input=sys.stdin.readline
# N,E= map(int,input().split())
#
# arr=[[] for _ in range(N)]
#
# for i in range(E):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
# visited=[False]*(N)
#
#
# ans=0
# def dfs(dep,x):
#     global ans
#     if dep==5:
#         ans=1
#         return #ans
#     # visited[x]=True
#
#     for i in arr[x]:
#         if visited[i]!=True:
#             dep+=1
#             dfs(dep,i)
#     visited[x]=False
# flag=0
# for i in range(N):
#     visited = [False] * (N)
#     g=dfs(1,i)
#     if g ==1:
#         flag=1
#         break
#
# if flag==1:
#     print(1)
# else:
#     print(0)


# 0~N-1

    import sys
    sys.setrecursionlimit(10000)
    input=sys.stdin.readline
    N,E= map(int,input().split())

    arr=[[] for _ in range(N)]

    for i in range(E):
        a,b=map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)

    visited=[False]*(N)


    ans=0
    def dfs(dep,x):
        global ans
        if dep==5:
            ans=1
            return #ans
        # visited[x]=True

        for i in arr[x]:
            if visited[i]!=True:
                dep+=1
                dfs(dep,i)
        visited[x]=False

    for i in range(N):
        # visited = [False] * (N)
        dfs(1,i)
        if ans:
            break
    if ans:
        print(1)
    else:
        print(0)