N=int(input())

D=[[0]*10 for _ in range(N+1)]
D[1]=[0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):

        if j==0:
            D[i][j]=D[i-1][j+1]

        elif j==9:
            D[i][j]=D[i-1][j-1]

        else:
            D[i][j]=D[i-1][j-1]+D[i-1][j+1]


print(sum(D[N])%1000000000)

