# 문제 번호 : 2588

a = int(input())
b = input()
for i in reversed(b):
    print(a*int(i))
print(a*int(b))