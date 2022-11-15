#채워야 할 acgt
checkArr =[0]*4
#내가 가진 acgt
myArr = [0]*4
#충족한 개수
checkSecret=0

def myadd(c):
    global checkArr,myArr,checkSecret
    if c=='A':
        myArr[0]+=1
        if myArr[0]==checkArr[0]:
            checkSecret+=1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1]==checkArr[1]:
            checkSecret+=1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c):
    global checkArr, myArr,checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

#문자열, 부분 문자열 길이
S,P = map(int,input().split())
Result=0
A=list(input())
checkArr=list(map(int,input().split()))

#순서 바뀌면 안됨, 이게 먼저 와야함!!!!!!!!!!!!
#0으로 이미 채워진 checkSecret 있는지도 확인
for i in range(4):
    if checkArr[i]==0:
        checkSecret+=1

# [첫번째 부분 문자열]
#첫번째 문자열 확인
for i in range(P):
    myadd(A[i])
#첫번째 부분 문자열 암호가 유효한지
if checkSecret==4:
    Result+=1

# [두번째부터 문자열 슬라이딩 시작]
for i in range(P, S):  # i=P,P+1,...S
    # j = 빠져야하는 처음 문자****
    j = i - P
    # i = 새롭게 더해지는 마지막 문자
    myadd(A[i])
    myremove(A[j]) #A[j] 아니고 j라 해서 디버깅
    # 다 충족했는지 확인
    if checkSecret==4:
        Result+=1 #Result=1로 해놔서 1시간 디버깅...
print(Result)







