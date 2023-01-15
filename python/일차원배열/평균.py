# 문제 번호 : 1546

n = int(input())
nums = list(map(int, input().split()))
a = max(nums)
new_nums = [(num*100)/a for num in nums]
print(sum(new_nums)/n)

