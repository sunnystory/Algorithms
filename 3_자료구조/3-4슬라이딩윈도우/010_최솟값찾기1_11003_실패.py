#11003 (틀림) -> 왜틀렸는지 모르겠음
# n,d=map(int,input().split())
# nums=list(map(int,input().split()))
# # en=0
# # st=en-d+1
# ans=[0]*n
# #최솟값 초기화
# min=5000001
# for i in range(0,-d,-1): #-1
#     # print(i)
#     if nums[i]<min:
#         min=nums[i]
#         # print(min)
# #min 초기화 됨
# ans[0]=min
# def find_min(st,en):
#     min = 5000001
#     # if st<0:
#     for i in range(st,en+1):
#         if nums[i]<min:
#             min=nums[i]
#     # else:
#     #     for i in range(st,en+1):
#     #         if nums[i]<min:
#     #             min=nums[i]
#     ans[en]=min
#     return min
# #end 값 슬라이딩 윈도우로 늘여가기
# for i in range(1,n):
#     en=i #1 #3
#     st = en - d + 1 #-1  #1
#     if nums[st-1]==min or nums[en-1]==min:
#         min=find_min(st,en)
#     else:
#         ans[i]=min
# for i in ans:
#     print(i, end=' ')


#BOOK - 정렬?? => FAIL
# n,d=map(int,input().split())
# nums=list(map(int,input().split()))
# current=nums[:]
# ans=[0]*n
# #최솟값 초기화
# min=5000001
# for i in range(0,-d,-1): #-1
#     # print(i)
#     if nums[i]<min:
#         min=nums[i]
#         # print(min)
# #min 초기화 됨
# ans[0]=min

#BOOK
from collections import deque
N,L=map(int,input().split())
mydeque=list(map(int,input().split()))
# 슬라이딩 윈도우, 데큐로 정렬 (최솟값 찾기 : 정렬 이용해서 푸는 문제 => idx랑 값 저장!)
now= deque([0,mydeque[0]]) #idx,num #
for i in range(1,N):
    if i-L+1>now[0][0]:
        now.popleft()
    #새로 들어오는 값이 제일 작으면 다 삭제, 들어오는 최솟값으로 초기화
    if now[0][1]>mydeque[i]:
        now=deque([i,mydeque[i]])

    #DIBUGGING : 마지막 위치에서 부터 삭제!!!***
    else:
        for k in range(1,len(now)):
            #첫번째 빼고 앞에서부터 삭제하면 덱이라 삭제가 어려움, 끝에서 부터 삭제!!!!!
            if now[k][1]>mydeque[i]:
                now.
        now.append([i,mydeque[i]])


    now.append([_,mydeque[_]])





#009번 다시 정리 할 것****
