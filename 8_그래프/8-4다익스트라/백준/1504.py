#1->v1 #v1->v2 # v2->1 다 더하기
import sys
input=sys.stdin.readline
u,v=map(int,input().split())
arr=[[] for _ in range(u+1)]

for _ in range(v):
    a,b,c=map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])


v1,v2=map(int,input().split())

import heapq
def djk(a,b):
    distances=[float('inf') for _ in range(u+1)]
    needvisit=[[0,a]] # w,n
    distances[a]=0
    # visited=[]
    # distances[]
    while needvisit:
        w,n=heapq.heappop(needvisit)
        if distances[n]<w:
            continue
        for n_n,n_w in arr[n]:
            distance=n_w+w
            if distances[n_n]>distance:
                distances[n_n]=distance
                heapq.heappush(needvisit, [distance,n_n])
    return distances[b]



d=djk(1,v1)+djk(v2,u)
e=djk(1,v2)+djk(v1,u)
result=min(d,e)+djk(v1,v2)
# 문제 조건 잘보기**=> 틀린 부분!!!!!!!!!!
print(result if result < float('inf') else -1)


# 도착지 필요 없긴함 ,,,, 출발지 distances return 후 인덱스로 값 뽑을 수도!!

# 다른 풀이
# # 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
# original_distance = dijkstra(1)
# #출발 v1/v2 각 노드로의 최단거리
# v1_distance = dijkstra(v1)
# v2_distance = dijkstra(v2)
#
# # 두 정점 들르는 경우 두가지
# v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
# v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]
#
# result = min(v1_path, v2_path)
# print(result if result < INF else -1)