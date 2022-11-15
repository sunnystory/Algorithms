#적절한 점화식 정의 필요
'''
L[N]=max(L[N-1]+A[i], A[i])
R[N]=max(R[N+1]+A[i], A[i])

* 왼쪽, 오른쪽 방향에서부터 해당 인덱스를 제거한 최대 연속 합 점화식!!
D[N]=L[N-1]+R[N+1]
'''


n=int(input())
A=[0]+list(map(int,input().split()))
# A.append[0]
# A=[0]+A
#arr=A[0]~A[n+1]
# print(A)
L=[-10000]*(n+1) #[0,0]
R=[-10000]*(n+2) #[0,0,0]
D=[0]*(n+1) #[0,0]


for i in range(1,n+1): #1,2,,,,n =>n+1-i
    L[i]=max(A[i],L[i-1]+A[i]) #L=[0,1]
    R[n+1-i]=max(A[n+1-i],R[n+2-i]+A[n+1-i])

for i in range(1,n+1):
    D[i]=L[i-1]+R[i+1]

# print(L)
# print(R)
# print(D)
D[0],L[0]=-10000,-10000
# print(L)
# print(R)
# print(D)
ans=max(max(L),max(D))

print(ans)


#반 례 !!!!!!!!!!!!!!
'''
1
-1
ans : -1
반례 찾기 너무 힘들었다.... 
D 배열 말고 L,R 초기화를 -10000으로 해줘야함!!
'''