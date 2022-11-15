n=int(input())
A=[0]*n

for i in range(n):
    A[i]=int(input())

num=1
stack=[]
answer=""
result=True
for i in A: #4 3 6 8
    while i >= num:
        stack.append(num)
        num += 1
        answer += '+\n'

    # if i==num:
    #     stack.pop()
    #     answer.append('-')

    if i<num:
        if stack.pop()==i:
            answer += '-\n'
        else:
            print('NO')
            result=False
            break

if result:
    print(answer)

