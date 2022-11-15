n=int(input())

# 동적계획법은 점화식!*** & MEMOIZATION

D=[-1]*1000001


D[1]=0
D[2]=1
D[3]=1

# for i in range(4,n+1):
#     if i%3==0:
#         D[i]=1+D[i//3]
#     elif i%2==0:
#         D[i]=1+D[i//2]
#     else:
#         D[i]=1+D[i-1]
#     print(i,'=',D[i])
for i in range(4,n+1):
    if i%3==0 and i%2==0:
        D[i]=min(1+D[i//3],1+D[i//2])
    elif i%3==0:
        D[i]=min(1+D[i//3],1+D[i-1])

    elif i%2==0:
        D[i]=min(1+D[i//2],1+D[i-1])
    else:
        D[i]=1+D[i-1]
    # print(i,'=',D[i])


print(D[n])