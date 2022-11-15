import copy
n=int(input())
jump=[[0]*2 for _ in range(n-1)]

for i in range(n-1):
    a, b = map(int, input().split())
    jump[i][0] = a
    jump[i][1] = b

dp=[0 for x in range(n+1)]

# 큰 점프와 작은 점프로 마지막 돌까지 가는 방법
# dp[1]=0
dp[2]=jump[1][0]
dp[3]=min(jump[1][1],jump[1][0]+jump[2][0])
# MIN=float('inf')

if n==1:
    print(0)
    exit()
elif n==2:
    print(jump[0][0])
    exit()


#4부터 dp 업데이트
if n>3:
    for x in range(4, n+1):
        dp[x]=min(dp[x-1]+jump[x-1][0],dp[x-2]+jump[x-2][1])


    #매우 큰 점프 적용 하는 경우
    K=int(input())
    dpcopy = copy.copy(dp)
    # 매우 큰 점프 뛸 수 있는 n-3까지
    for x in range(1, n-2): #n-3
        # dpcopy = dp[:]
        #매우 큰 점프한게 더 작으면 전체 업데이트 필요
        if dp[x] + K <dp[x+3]:
            dpcopy[x+3]=dp[x]+K

            #다음 값들 업데이트
            for t in range(x+4,n+1):
                dpcopy[t]=min(dp[t],dpcopy[t-1]+jump[t-1][0],dpcopy[t-2]+jump[t-2][1])
#
#         if MIN>dpcopy[-1]:
#             MIN=dpcopy[-1]
#
# if MIN==float('inf'):
#     print(dp[-1])
# else:
#     print(MIN)

print(min(dp[-1],dpcopy[-1]))



# if n==1:
#     print(0)
#     exit()
# if n==2:


