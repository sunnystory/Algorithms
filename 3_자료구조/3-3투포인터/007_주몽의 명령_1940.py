# 내맘대로 하는 걸 좋아해서 잘 해야하만 해 그게 뭐든

#my
n=int(input())
m=int(input())
ids=list(map(int,input().split()))
ids.sort() #디버깅, 까먹음
ans=0
# print(ids)
start,end=0,n-1
while start<end: #디버깅 #start!=end:#start!=n-1 or end!=1:
    if ids[start]+ids[end] <  m :
        start+=1
    elif ids[start]+ids[end] >  m :
        end-=1
    else :
        ans+=1
        start+=1
        end-=1
print(ans)






# [dibugging]
# 양쪽 pointer를 어디에다 둬야하는지 고민
# 정렬은 생각 O
# 값이 같을때 포인터 옮기는 규칙 생각 X
# [이동 원칙]
# 숫자 리스트 A, 만들어야 하는 수 M
#1)
#2)
#3)
#=> 값이 같을때 양쪽 포인터 모두 움직여야 함 ; 더이상 각각의 조합으로 원하는 수를 만들 수가 없으므로 (서로한테 유일한 조합)
#9 =2+7 (7로 9를 만들 수 있는 다른 조합은 없음)

#book
#pointer를 양쪽 끝에 두는게 핵심!!!!!
#pointer 순서/생각 차이 => 전에 문제랑 비교하기
#코테 즐겁고 흥미로운 마음으로 풀 수 있을 정도로 연습!!!!!