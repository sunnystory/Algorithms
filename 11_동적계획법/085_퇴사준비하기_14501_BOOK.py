# 거꾸로 생각!

# 초기화
# Memo=D
# D[i] : "i번쨰 날부터 퇴사날까지 벌 수 있는 최대 수입"

# 알고리즘
# 오늘 시작되는 상담이 퇴사일까지 끝나지 않는 경우
# D[i]=D[i+1]
# i+1번쨰 날부터 퇴사날까지 벌 수 있는 수입
# 오늘 시작되는 상담이 퇴사일 안에 끝나는 경우
# D[i]=Max(D[i+1], D[i+T[i]]+P[i])
# D[i]=Max(i+1번쨰 날부터 퇴사날까지 벌 수 있는 수입, 지금 날짜 벌 수 있는 수입 + 지금 날짜에 소요되는 시간 이후에 벌수 있는 수입)

# 결과
# D[1]값 출력

import sys
input=sys.stdin.readline
N=int(input())
#퇴사일까지 벌 수 있는 최대 수입
D=[0]*(N+2)
#상담에 필요한 일수
T=[0]*(N+1)
#상담 완료시 수입
P=[0]*(N+1)


for i in range(1,N+1):
    T[i],P[i]=map(int,input().split())

#감소하는 리스트 주의**
for i in range(N,0,-1):
    if i+T[i]>N+1:
        D[i]=D[i+1]
    else:
        D[i]=max(D[i+1], D[i+T[i]]+P[i])

print(D[1])