from collections import deque

n=int(input())
arr=list(input())

lr=deque()
sk=deque()

# lr,sk=[],[]

num=0

for i in arr:
    if i=='L':
        lr.append(1)

    elif i=='R':
        if len(lr)==0:
            break
        else:
            num+=1
            lr.pop()
    elif i=='S':
        sk.append(1)
    elif i=='K':
        if len(sk)==0:
            break
        else:
            num+=1
            sk.pop()
    else:
        num+=1

print(num)
