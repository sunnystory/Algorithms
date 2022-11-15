N,K=map(int,input().split())

stuff=[[0,0]]
for i in range(N):
    stuff.append(list(map(int,input().split())))

# print(stuff)

#memo
memo=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w,v=stuff[i]
    for j in range(1,K+1):
        if j<w:
            memo[i][j]=memo[i-1][j]
        else:
            memo[i][j]=max(memo[i-1][j],memo[i-1][j-w]+v)
    # print(memo[i])

print(memo[-1][-1])
