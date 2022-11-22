import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

N=int(input())

def isPrime(n):
    for i in range(2,int(n/2+1)):
        if n%i==0:
            return False
    return True

def dfs(n):
    '''DIBUGGING & IDEA : len(str(n))로 자리수 판별!!!!'''
    if len(str(n))==N:
        print(n)

    else:
        '''set으로 구현해야 시간초과 안뜸'''
        for i in (1,3,7,9):
            num=n*10+i
            if isPrime(num):
                dfs(num)
        '''시간 초과 안뜬 이유 : range로 구현돼서'''
        # for i in range(1,10):
        #     if i %2 ==0:
        #         continue
        #     if isPrime(n*10+i):
        #         dfs(n*10 + i)

'''왼쪽에서부터 시작해서 1의자리 + 2의자리...가능한 경우의 수 더해가는 dfs 방식'''

dfs(2)
dfs(3)
dfs(5)
dfs(7)