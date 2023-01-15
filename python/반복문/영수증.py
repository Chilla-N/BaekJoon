# 문제 번호 : 25304

entire = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a*b

if sum == entire:
    print("Yes")
else:
    print("No")
