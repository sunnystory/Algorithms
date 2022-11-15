n=int(input())
A=list(map(int,input().split()))
stack=[]
Onum=[0]*n
# for i in range(n):
#     if len(stack)==0:
#         stack.append((i,A[i])) #idx,값
#     elif stack[-1][1]<A[i]:
#         while stack and stack[-1][1]<A[i]: #stack이 있는지 확인 해줘야함,,, pop하다보면 다 빠질 수가 있어서 append 하기전에!!
#             idx,num=stack.pop()
#             Onum[idx]=A[i]
#         stack.append((i,A[i]))
#     elif stack[-1][1]>A[i]: #else하면 같은 거 엌케?,,
#         stack.append((i,A[i]))

# for i in range(n): # 4 # 3 5 2 7
#     if len(stack)==0:
#         stack.append((i,A[i])) #idx,값
#     while stack[-1][1]<A[i]:
#         idx,num=stack.pop()
#         Onum[idx]=A[i]
#     stack.append((i,A[i]))

#왜 STACK으로 이뤄져 있는지 이해 => 먼저 들어간 값은 그 다음 값보다 항상 더 크므로 pop()해줘서 비교
# 그 밑에 수들은 당연히 pop()보다 크므로
# while pop()이 현재 노드 값보다 작은부터 탐색 해주고 차례로 아래 값들도 탐색
for i in range(n): # 4 # 3 5 2 7
    # if len(stack)==0:
        # stack.append((i,A[i])) #idx,값
    #DIBUGGING POINT : while stack
    while stack and stack[-1][1]<A[i]: # 0 1 2 3
        idx,num=stack.pop()
        Onum[idx]=A[i]
    stack.append((i,A[i]))


for i in range(n):
    if Onum[i]==0:
        Onum[i]=-1

for i in Onum:
    print(i,end=' ')