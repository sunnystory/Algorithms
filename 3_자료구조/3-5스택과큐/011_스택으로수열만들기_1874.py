#1~n
n=int(input())

#push + pop - NO

# arrs=[i for i in range(1,n+1)]
stack=[]
ans=[]

k = 0
# for _  in range(n):
#     n=int(input())
#     while stack==[] or stack[-1]!=n:
#         print('+')
#         stack.append(k)
#         k+=1
#     stack.pop()
#     print('-')

flag=0
for _  in range(n):
    n=int(input())
    if len(stack)==0:
        k+=1
        stack.append(k)
        ans.append('+')
    while stack[-1]<n: #while 사용 - 조건 충족할때까지 반복하고 싶을때!!
        k+=1
        stack.append(k)
        ans.append('+')

    if stack[-1]==n:
        stack.pop()
        ans.append('-')

    # els:
    elif  stack[-1]>n:
        flag=1
        break

if flag==0:
    for i in ans:
        print(i)
    # print(ans,end='\n')
else:
    print('NO')