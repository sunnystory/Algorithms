#틀림 또 틀림!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import sys
input=sys.stdin.readline
import heapq
n,m,k=map(int,input().split())
arr=[ [] for _ in range(n+1)]

for _ in range(m):
    a,b,s=map(int, input().split())
    arr[a].append([b,s]) #n,w

# k번째 최단경로 소요시간
# 1차원이 아닌 k개의 최단거리 원소를 갖는 2차원 리스트 형태
distances=[[float('inf')]*k for _ in range(n+1)]


def dajk():
    distances[1][0]=0
    needvisit=[[0,1]] #가중치 우선 : 거리, 노드 순

    #k번째 경로를 찾기 위해 노드가 여러번 쓰이므로
    #기존 다익스트라 로직에서 사용한 노드 방문 리스트를 체크하는 부분은 삭제 필요

    while needvisit:
        #우선순위큐에서 노드와 가중치 가져옴
        w,n=heapq.heappop(needvisit)


        # if w < distances[n][-1]: #틀림 : 체크 필요 없음 : 이미 더 작아서 들어갔고, 여기서는 이미 방문한 visited 길이 확인 안해줄 거니까
        # 연결노드 k번째 경로와 신규 경로 비교
        for n_n,n_w in arr[n]:
            distance=n_w+w
            # 신규 경로가 더 작을때 , 업데이트, 거리 배열 오름차순으로 정렬
            if distance<distances[n_n][-1]:
                distances[n_n][-1]=distance
                distances[n_n].sort()
                # 우선순위 큐에 노드 추가
                heapq.heappush(needvisit,[distance,n_n])

dajk()

for _ in range(1,n+1):
    t=distances[_][k-1]
    if t==float('inf'):
        print(-1)
    else:
        print(t)






