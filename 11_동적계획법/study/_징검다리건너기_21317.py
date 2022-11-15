N=int(input())
jump=[]

#dp 생성
dp=[float('inf')]*N

for i in range(N-1):
    one,two=map(int,input().split())
    jump.append((one,two))
    if i+1 <N:
        dp[i+1]=min(dp[i+1],dp[i]+one)
    if i+2 <N:
        # dp[i+2]=min(dp[i+2],dp[i]+two)
        dp[i+2]=dp[i]+two

#매우 큰 점프 적용해 최솟값 다시 찾기
K=int(input())
_min=dp[-1]

# 매우 큰 점프를 뛸 수 있는 돌의 경우 모두 저장
for i in range(3,N):
    # 매우 큰를 해당 돌에서 뛴 값, +1점프 업데이트 할 값, +2점프 업데이트 할 값
    e,dp1,dp2=dp[i-3]+K, float('inf'), float('inf')
    # 매우 큰 점프 이후부터 +1,+2 점프로 최소값 다시 업데이트
    for j in range(i,N):#3,4,5,...
        #+1해서 ~N번쨰 돌까지 가는 값 업데이트
        if i+1<N: #4
            dp1=min(dp1,e+jump[j][0]) # (가장큰뜀) + (다음+1) 경우나 dp2로 온 경우 비교, 업데이트
        #+2해서 ~N번째 돌까지 가는 값 업데이트
        if i+2<N:
            dp2=e+jump[j][1]
        #각 경우 업데이트해서 이전 dp1(1계단 간 값이랑 비교)
        e,dp1,dp2=dp1,dp2,float('inf')
    _min=min(_min,e)

print(min)
