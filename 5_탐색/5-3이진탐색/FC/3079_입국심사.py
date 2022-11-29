import sys
input=sys.stdin.readline
N,M=map(int,input().split()) #심사대, 친구
arr=[int(input()) for _ in range(N)]

# for i in range(N):
#     arr.append(int(input()))

l,r = min(arr), max(arr)*M # 걸리는 시간 최대값
ans=r

#arr=[2,3,3,4,6,8,9] #2, 20

while l<=r:
    total=0
    mid=(l+r) // 2 #11분 # 최단시간을 중간값 이용해서 구하기

    for i in range(N): #7
        total+=mid//arr[i] #11분간 첫번째~마지막 심사대에서 몇명 심사할 수 있을지 구하는 것
        # 11//2=5 =>total=5 , 11//3=3 =>total =8

    if total >=M:
        r=mid-1
        ans=min(mid,ans)

    else:
        l=mid+1

print(ans)




