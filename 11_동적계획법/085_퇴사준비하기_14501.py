import sys
input=sys.stdin.readline

N=int(input())
arr=[[0,0]]
for _ in range(N):
    # T,P
    arr.append(list(map(int,input().split())))

memo=[[0]*(N+1) for _ in range(N+1)]
# print(arr)
# print(memo)
for now in range(1,N+1):
    w,v=arr[now]

    if w+now-1< N+1 :
        memo[now][now+w-1]=max(memo[now-1][now+w-1],memo[now-1][now-1]+v)
        for j in range(now+w-1,N+1):
            valu=memo[now][now + w - 1]
            memo[now][j]=valu
        for j in range(1, now + w - 1):
            memo[now][j] = memo[now - 1][j]
    else:
        memo[now]= memo[now - 1]


    #
    # for j in range(1,N+1):
    #     memo[i][i+w-1]=
    #
    #     if i+w<N+1:
    #         memo[i+w][j]=max(memo[i-1][j],memo[i-1][w+i]+memo[i-1][w-1])
# print(memo)
print(memo[-1][-1])

