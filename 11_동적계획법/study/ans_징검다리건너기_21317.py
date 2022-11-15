
n=int(input())
# 0~n-2 : 1번돌~n-1번돌까지
mlist=[[0]*2 for _ in range(n-1)]
for i in range(n-1):
    a, b=map(int,input().split())
    mlist[i][0]=a
    mlist[i][1]=b

k=int(input())

if n==1:
    print(0)
    exit()
elif n==2:
    print(mlist[0][0])
    exit()

#dp 0~n-1 :1번돌~n번돌까지
dp=[0]*n

# 2~3번 돌 가는 방법
dp[1]=mlist[0][0] #2번돌 = 1번돌+1
dp[2]=min(mlist[0][0]+mlist[1][0], mlist[0][1]) #3번돌 = (1번돌+1) + (2번돌+1) or (1번돌+2)

res=dp[-1]

# 4번~마지막 돌을 갈 수 있는 방법:
# 1. 큰 점프와 작은 점프로 마지막 돌까지 가는 방법
# 전전 돌을 가는 벙법+전 돌에서 작은 점프, 전전전 돌을 가는 방법+전전 돌에서 점프 중 작은 값
for i in range(3, n):
    dp[i]=min(mlist[i-1][0]+dp[i-1], mlist[i-2][1]+dp[i-2])
#최소값
res=dp[-1]

# 2. 매우 큰 점프 적용 하는 경우
dp2=dp[:] #매우 큰 점프시 dp
for i in range(0, n-3):
    #dp[i]+k의 값이 i에서 매우 큰 점프를 한 곳의 원래의 값인 dp[i+3]보다 작으면 전체 업뎃
    #=> 매우 큰 점프한게 더 작으면 전체 업데이트 필요
    if dp[i]+k<dp[i+3]:
        dp2[i+3]=dp[i]+k
        #새로 dp를 계산
        for j in range(i+4, n):
						#+1/+2 경우 중 작은값 업뎃
            dp2[j] = min(dp2[j - 1] + mlist[j - 1][0], dp2[j - 2] + mlist[j - 2][1])

        #원래 결과와 비교하여 더 작은 값
        if dp2[-1]<res:
            res=dp2[-1]
print(res)


##################
# 위에거랑 같은 풀이!
# n=int(input())
# mlist=[[0]*2 for _ in range(n-1)]
# for i in range(n-1):
#     a, b=map(int,input().split())
#
#     mlist[i][0]=a
#     mlist[i][1]=b
#
# k=int(input())
#
# if n==1:
#     print(0)
#     exit()
# elif n==2:
#     print(mlist[0][0])
#     exit()
# dp=[0]*n
#
# # 큰 점프와 작은 점프로 마지막 돌까지 가는 방법
# dp[1]=mlist[0][0]
# dp[2]=min(mlist[0][0]+mlist[1][0], mlist[0][1])
#
# #3번~마지막 돌을 갈 수 있는 방법: 전전 돌을 가는 벙법+전 돌에서 작은 점프, 전전전 돌을 가는 방법+전전 돌에서 점프 중 작은 값
# res=dp[-1]
#
# if n>3:
#     for i in range(3, n):
#         dp[i]=min(mlist[i-1][0]+dp[i-1], mlist[i-2][1]+dp[i-2])
#
#     res=dp[-1]
#     dp2=dp[:]
#     # 매우 큰 점프 적용 하는 경우
#     for i in range(0, n-3):
#         # 매우 큰 점프한게 더 작으면 전체 업데이트 필
#         #dp[i]+k의 값이 i에서 매우 큰 점프를 한 곳의 원래의 값인 dp[i+3]보다 작으면
#         if dp[i]+k<dp[i+3]:
#             dp2[i+3]=dp[i]+k
#             #새로 dp를 계산
#             for j in range(i+4, n):
#                 dp2[j] = min(dp2[j - 1] + mlist[j - 1][0], dp2[j - 2] + mlist[j - 2][1])
#
#             #원래 결과와 비교하여 더 작은 값
#             if dp2[-1]<res:
#                 res=dp2[-1]
#
#
# print(res)
#


#1+1 2
# dp[3]=min(dp[2]+mlist[2][0],dp[1]+mlist[1][1])