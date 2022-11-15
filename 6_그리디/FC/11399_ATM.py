import sys
input=sys.stdin.readline

##### 내코드 #####
N=int(input())
arr=list(map(int,input().split()))
arr.sort()

sumli=[] #list 변수명 sum으로 하지 않게 주의**
for i in range(len(arr)): #range(길이 값인지 리스트인지 확인!!)
    sumli.append(sum(arr[:i+1]))
print(sum(sumli))

##### 강의 코드 #####
N=int(input())
arr=list(map(int,input().split()))
arr.sort()

#바로 변수에다가 합 구해서 더 빠름!!
minimum=0
for i in range(N):
    for j in range(i+1):
        minimum+=arr[j]
print(minimum)
#################
