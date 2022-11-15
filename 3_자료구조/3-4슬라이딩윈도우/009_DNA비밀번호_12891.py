'''슬라이딩 윈도우 알고리즘
2개의 포인터로 범위 지정, 범위를 유지한채로 이동해 문제를 해결
'''
#009
#'A' 'C' 'G' 'T'
# 임의의 DNA 문자열 만들고 부분 문자열을 비밀번호로 사용

#'문자의 개수가 특정 개수 이상이어야 비밀번호를 사용'
'''DNA 문자열, 비밀번호 길이, 몇번 이상, 
비밀번호 종류의 수 
부분문자열 위치 다르면 다른 문자열'''

#MY(book 참고)
# s - 문자열 길이 / p - 비번으로 사용할 부분 문자열 길이
s,p=map(int,input().split())
#'A','C','G','T' 로 구성된 dna 문자열
dna=list(input())
#'A','C','G','T' 최소 개수
acgt=list(map(int,input().split()))
#현재 상태 리스트를 만들어 빠지고/더해지는 문자열을 업데이트 해가면서 비교
#업데이트 방식*** : 빠지는 문자열, 신규 문자열만 보고 업데이트!!
current=[0,0,0,0]
st,en=0,p-1
ans=0
#현재 상태 초기화 - 처음 비번 사용문자열로
for i in range(p): #p-1까지
    if dna[i]=='A':
        current[0]+=1
    elif dna[i]=='C':
        current[1]+=1
    elif dna[i]=='G':
        current[2]+=1
    else:
        current[3]+=1
#시작&끝 슬라이딩 윈도우로 이동하기
while True : #st<=s-p and en<=s-1: #슬라이딩 가능 범위 내에서 업뎃
    flag=0
    #문자열 유효한지 확인
    for i in range(4):
        if current[i]<acgt[i]:
            flag=1
        if flag==1:
            break
    if flag==0:
        ans+=1
    # 빼고 my remove
    first=dna[st]
    if first=='A':
        current[0]-=1
    elif first=='C':
        current[1]-=1
    elif first=='G':
        current[2]-=1
    else:
        current[3]-=1
    #슬라이딩 윈도우 업데이트
    st += 1
    en+=1
    if en>s-1:
        break
    # 더하기 my add
    last=dna[en]
    if last=='A':
        current[0]+=1
    elif last=='C':
        current[1]+=1
    elif last=='G':
        current[2]+=1
    else:
        current[3]+=1
    #dictionary 구현..? 고민해보기***
print(ans)

