n,m=map(int,input().split()) #문자열9,  부분문자열8
dna=list(input()) #[C,C,T,G,G,A]
acgt=list(map(int,input().split())) #[2,0,1,1]
first=[0,0,0,0]

#첫 슬라이딩 저장
for i in range(m):
    if dna[i]=='A':
        first[0]+=1
    elif dna[i]=='C':
        first[1]+=1
    elif dna[i]=='G':
        first[2]+=1
    elif dna[i]=='T':
        first[3]+=1
flag = 0
ans=0
for _ in range(4):
    if first[_] >= acgt[_]:
        flag += 1
if flag == 4:
    ans = 1

def sub_f(x):
    if x == 'A':
        first[0] -= 1
        # return 0
    elif x == 'C':
        first[1] -= 1
        # return 1
    elif x == 'G':
        first[2] -= 1
        # return 2
    elif  x == 'T':
        first[3] -= 1
        # return 3

def plus_l(x):
    if x == 'A':
        first[0] += 1
    elif x == 'C':
        first[1] += 1
    elif x == 'G':
        first[2] += 1
    elif x == 'T':
        first[3] += 1


# 슬라이딩 옆으로 이동
for i in range(1,n-m):
    f_l=dna[i-1]
    l_l=dna[i+m-1]
    sub_f(f_l)
    plus_l(l_l)

    flag=0
    for _ in range(4):
        if first[_]>=acgt[_]:
            flag+=1

    if flag==4:
        ans+=1

print(ans)