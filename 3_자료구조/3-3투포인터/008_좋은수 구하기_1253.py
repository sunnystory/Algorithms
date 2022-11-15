# #008
# #wrong!! => 문제 조건 : 절대값이므로 음수일 때 고려 필요
# # 반례
# # 3
# # -5 -2 -3
# # 정답 1
# # 3
# # 0 0 0
# # 정답 3
# # 3
# # 0 0 1
# # 정답 0
#
# n=int(input())
# nums=list(map(int,input().split()))
# nums.sort()
#
# # nums.reverse()
# # num_re=list(reversed(nums))
# # print(num_re)
#
# # st,en=0,n-2
# # ans=0
# # for i in num_re: #[10,9,8,7...]
#
#
# ans=0
# for i in range(2,n):
#     st, en =0,i-1
#     while st<en:
#         if nums[st]+nums[en]<nums[i]:
#             st+=1
#         elif nums[st]+nums[en]>nums[i]:
#             en-=1
#         else:
#             ans+=1
#             break
# print(ans)



#Dibugging
#음 수 일때는 양수까지 고려를 해야함.
# 포인터


#BOOK
n=int(input())
nums=list(map(int,input().split()))
nums.sort()
ans=0
for i in range(n):
    st, en =0,n-1

    while st<en:
        if nums[st]+nums[en]<nums[i]:
            st+=1
        elif nums[st]+nums[en]>nums[i]:
            en-=1
        else:
            # 자기 자신 포함하면 안됨*****
            if st==i :
                st+=1
            elif en==i:
                en-=1
            else:
                ans+=1
                break
print(ans)
