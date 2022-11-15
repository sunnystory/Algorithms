#my => 시간초과
# import sys
# input=sys.stdin.readline
# m,n=map(int,input().split())
# nums=list(map(int,input().split()))
#
# ans=0
# temp=0
# D=[]
# for _ in nums:
#     temp+=_
#     D.append(temp)
#
# for _ in D:
#     if _%n==0:
#         ans+=1
#
# for i in range(m-1):
#     for j in range(i+1,m):
#         if (D[j]-D[i])%n==0:
#             ans+=1
#
# print(ans)

#book
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
#A : 원본 수열 리스트
A=list(map(int,input().split()))

#1. 합 배열 D를 구한다. => D이용해 A도 구할 수 있고, 구간합도 구할 수 있음
D=[]
temp=0
for i in A:
    temp+=i
    D.append(temp)

#2. 합 배열 D를 m로 나눈 나머지 배열 S를 구한다.
# D[i]%m 의 값과 D[j]%m의 값이 같다면 (D[i]-D[j])%m은 0이다.
# 구간 합 배열의 원소를 m으로 나눈 나머지로 업뎃 후 S[i], S[j]가 같은 (i,j) 쌍을 찾으면
# 원본 리스트 j+1~i까지의 구간합의 m으로 나눠 떨어진다.

# C 선언 : 같은 나머지의 인덱스를 카운트 하는 리스트 ; 인덱스가 나머지 값이 됨
# 나머지가 같은 원소 중 2개 선택할 경우의 수(구간 합 경우의 수) 구함
# => 조합으로 구한다. ex) 1,2,0,1,1 : 1로 나머지가 같은 3개의 구간합 중 2개를 선택할 경우의 수

#3. C 선언
# 합 배열로 나머지가 같은 값 카운트 하는 C리스트를 구한다.

C=[0]*m
ans=0
for i in D:
    left=i%m
    if left==0:
        ans+=1
    C[left]+=1
for i in C:
    ans+=i*(i-1)//2

print(ans)



