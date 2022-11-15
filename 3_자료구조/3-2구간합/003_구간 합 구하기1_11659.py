# N, M = map(int, input().split())
# nums=list(map(int,input().split()))
#
# sum_nums=[0]*(N+1)
#
# for k in range(1,N+1):
#     sum_nums[k]=sum_nums[k-1]+nums[k-1]
# for _ in range(M):
#     a,b=map(int,input().split() )
#     if a>1:
#         print(sum_nums[b]-sum_nums[a-1])
#     else:
#         print(sum_nums[b])


#book
import sys

input=sys.stdin.readline
m,n=map(int,input().split())
sum_nums=[0] #index 0인 부분은 0으로 저장

nums=list(map(int,input().split()))
# for _ in range(m):
#     sum_nums.append(sum_nums[_]+nums[_])

#temp 활용하기**
temp=0
for i in nums:
    temp+=i
    sum_nums.append(temp) #합 배열 만들기

for _ in range(n):
    a,b=map(int,input().split())
    print(sum_nums[b]-sum_nums[a-1]) #합 배열에서 구간 합 구하기



