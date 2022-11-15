#my - 생각 못함


# book
# 투포인터로 풀기
# start_index & end_index
# count=1
# sum=1

# 1부터 어떠한 자연수 N까지 자연수의 합 구하기
# if sum < num : sum+=end_index++ ; end_index++
# if sum > num : sum-=start_index ; start_index++
# if sum==num : count+=1 ; end_index++


n=int(input())
start,end=1,1
count=1
sum=1

#n이 포함돼서 더해질 때는 당연히 n보다 클 수밖에 없고, 초기화시 n일때 값을 카운트 해줬으니까 n보다 작을때 까지만 돌기
while end<n: # #while end!=n: 랑 같음
    if sum<n:
        end+=1
        sum+=end # sum이 n보다 작을때는 end값 업데이트 한 후에 sum에다가 end 더해줌
    elif sum>n:
        sum-=start # sum 이 n보다 클때는 sum에서 start 먼저 뺴준 후에 start값 업데이트
        start+=1
    else:
        count+=1
        end+=1
        #**** 디버깅 부분****#
        sum+=end #같을때 sum값 +end로 업데이트 안해줘서 틀림


print(count)