# my
n=int(input())
scores=list(input().split())

avg=0
for _ in range(len(scores)):
    scores[_]=int(scores[_])
best=max(scores)
for i in scores:
    avg+=i/best*100

print(avg/len(scores))


#book
#(A/M*100 + B/M*100 + C/M*100) / 3 = (A+B+C)*100/M/3
#=> 한 과목과 관련된 수식을 총합한 후 관련 수식으로 변환해 로직을 간단하게 할 수 있음
n=int(input())
mynums=list(map(int, input().split()))
mymax=max(mynums)
ans=sum(mynums)*100/mymax/n
print(ans)