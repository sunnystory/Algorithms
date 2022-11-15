#혼자 못품
#책 참고

from collections import deque

n=int(input())
A=list(map(int,input().split()))
# stack=deque([(0,arr[0])])

# #3
#
# #3 5 2 7
# for i in range(len(arr)):
#     now=arr[i]
#     while stack[0][1]<=now:
#
#     if arr[i]>first:
#         stack.append((i,arr[i])) #idx, 값

stack=[]
ans=[0]*n
#idx
for i in range(n):
    while stack and A[ij                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 koy]>A[stack[-1]]:#
      ans[stack.pop()]=A[i]
    stack.append(i)
while stack:
    ans[stack.pop()]=-1

result=""

for i in range(n):
    result +=str(ans[i])+" "

print(result)




