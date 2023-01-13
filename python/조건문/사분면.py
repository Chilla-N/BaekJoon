# 문제 번호 : 14681

a = int(input())
b = int(input())

if a > 0:
    if b > 0:
        print(1)
    else:
        print(4)
elif b > 0:
    print(2)
else:
    print(3)