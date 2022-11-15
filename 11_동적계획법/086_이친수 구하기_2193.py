N=int(input())

arr=[[0]*2 for _ in range(N+1)]

arr[1]=[0,1]
arr[2]=[1,0]

for i in range(3,N+1):
    arr[i][0]=arr[i-1][0]+arr[i-1][1]
    arr[i][1]=arr[i-1][0]

print(sum(arr[-1]))

