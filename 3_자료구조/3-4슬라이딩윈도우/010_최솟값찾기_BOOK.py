# BOOK
from collections import deque

#A[i-(L-1)] ~ A[i] => sliding window 크기가 "L"이다
#A[i-L+1] ~ A[i] 중 최솟값 D[i] 구하기
N,L=map(int,input().split())#숫자, 슬라이딩 윈도우 크기
A=list(map(int,input().split()))

#BOOK
mydeq=deque([]) # mydeq=deque() => 둘이 같은 것
for i in range(N):
    while mydeq and mydeq[-1][0]>A[i]:
        mydeq.pop()

    #DIBUGGING => deque 내 리스트로 구현시 시간초과
    #=> set으로 구현해야함
    # mydeq.append([A[i],i])
    mydeq.append((A[i], i))
    if mydeq[0][1]<i-L+1:
    # if mydeq[0][1] <= i - L :
        mydeq.popleft()
    print(mydeq[0][0], end=' ')




#실패 흔적
# from collections import deque
#
# #A[i-(L-1)] ~ A[i] => sliding window 크기가 "L"이다
# #A[i-L+1] ~ A[i] 중 최솟값 D[i] 구하기
# N,L=map(int,input().split())#숫자, 슬라이딩 윈도우 크기
# A=list(map(int,input().split()))
#
#
# # 덱에 (인덱스,값)으로 저장
# # 새로 들어오는 값이랑 비교하면서 구현
# # mydeque=deque([[0,A[0]]])
# # print(mydeque[0][1], end=' ')
#
# mydeque=deque([])
# for i in range(N):
#     new=[i,A[i]]
#
#     for j in range(len(mydeque)-1,-1,-1):
#         if mydeque[j][1]>=new[1]:
#             mydeque.pop()
#         else:
#             break
#     mydeque.append(new)
#     if mydeque[0][0] < (i-L+1) :
#         mydeque.popleft()
#     print(mydeque[0][1], end=' ')
#
# '''
# #최댓값
# m=max(A)
# #A[k] 중 k<0인거는 무시하고 최솟값 D를 구할 것
# # 첫번째 슬라이딩 윈도우
# sl=[m]*L
# sl[L-1]=A[0]
# D=[m]*L
# D[0]=A[0]
# '''
#
# # i : 0~(N-1)

# # deque로 최소값 수 슬라이딩 이동하면서 찾기 구현
# mydeq=deque([])
# ans=[A[0]]
# for i in range(N):
#     mydeq.append([A[i],i])
#     if mydeq[0][1]<i-L+1:
#         mydeq.popleft()
#     while

