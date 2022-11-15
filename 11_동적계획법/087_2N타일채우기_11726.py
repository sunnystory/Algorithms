import sys
input=sys.stdin.readline
# 087
#D[n]=D[n-1]+D[n-2]
#so easy one~~~

N=int(input())

#############DIBUGGGGGINGGGG########################
#인덱스 에러 나는 부분 ***********초기화 행렬 주의 그냥 전체 값으로 줄것
# D=[0]*(N+1)
##########################################################
D=[0]*(1001)
D[1]=1
D[2]=2

for i in range(3,N+1):
    D[i]=(D[i-1]+D[i-2])

print(D[N]%10007)

# if n>=2:
#     cache[2] = 2
#     for i in range(3,n+1):
#         cache[i]=cache[i-2]+cache[i-1]
#
# print(cache[n]%10007)




